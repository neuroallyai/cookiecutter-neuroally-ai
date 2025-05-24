import os
import subprocess
import sys
import shutil
from pathlib import Path

# --- Configuration & Globals ---
PROJECT_DIR = Path(os.getcwd())
# These variables are templated by Cookiecutter
SLUG = "{{ cookiecutter.project_slug }}"
USE_CONDA = "{{ cookiecutter.use_conda_support }}" == "yes"

# --- Conditional Debug Printing ---
if os.environ.get("PROJECT_SETUP_DEBUG"):
    print(f"DEBUG: Script running in: {Path(__file__).parent}")
    print(f"DEBUG: Current working directory (project root): {PROJECT_DIR}")
    print(f"DEBUG: Files in project root: {os.listdir(PROJECT_DIR)}")
    print(f"DEBUG: Looking for pyproject.toml at: {PROJECT_DIR / 'pyproject.toml'}")
    print(f"DEBUG: Project slug: {SLUG}")
    print(f"DEBUG: Use Conda: {USE_CONDA}")


# --- Helper Functions ---
def run(command_args, **kwargs):
    """
    Runs a command using subprocess.
    'command_args' can be a string (which will be run with shell=True)
    or a list of arguments (which will be run with shell=False).
    """
    is_shell_command = isinstance(command_args, str)

    # Prepare display string for logging
    if is_shell_command:
        cmd_display_str = command_args
    else:
        cmd_display_list = []
        for arg in command_args:
            if " " in str(arg):  # Ensure arg is string for 'in' check
                cmd_display_list.append(f'"{arg}"')
            else:
                cmd_display_list.append(str(arg))
        cmd_display_str = " ".join(cmd_display_list)

    print(f"→ {cmd_display_str}")

    try:
        # Pass cwd explicitly to ensure commands run in the project directory
        # This is generally safer than os.chdir.
        subprocess.run(
            command_args, shell=is_shell_command, check=True, cwd=PROJECT_DIR, **kwargs
        )
    except FileNotFoundError as e:
        # Try to provide a more helpful error if a command isn't found
        cmd_name = command_args if is_shell_command else command_args[0]
        print(
            f"❌ Error: Command '{cmd_name}' not found. Please ensure it's installed and in your PATH."
        )
        print(f"   Details: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd_display_str}")
        print(f"   Return code: {e.returncode}")
        if e.stdout:
            print(f"   Stdout: {e.stdout.decode(errors='ignore')}")
        if e.stderr:
            print(f"   Stderr: {e.stderr.decode(errors='ignore')}")
        # The main exception handler will catch this and exit if this function doesn't.
        raise  # Re-raise to be caught by the main try-except block


def ensure_poetry_installed():
    """Ensure Poetry is installed system-wide or user-wide before continuing."""
    if shutil.which("poetry") is None:
        print("Poetry not found. Attempting to install Poetry using pip...")
        print(
            "If this fails, please install Poetry manually: https://python-poetry.org/docs/#installation"
        )
        try:
            run(["pip", "install", "--user", "poetry"])
            # Note: User might need to ensure the user script path is in their system PATH.
            print(
                "✅ Poetry installed via pip. Please ensure your PATH is configured correctly."
            )
            print("   You might need to open a new terminal session.")
            if shutil.which("poetry") is None:
                print(
                    "   WARNING: Poetry still not found in PATH after pip install --user."
                )
                print(
                    "            Please verify your PATH or install Poetry using the official installer."
                )
        except Exception as e:
            print("❌ Failed to install Poetry using pip.")
            print(
                "   Please install Poetry manually: https://python-poetry.org/docs/#installation"
            )
            sys.exit(1)
    else:
        print("✅ Poetry already installed.")


# --- Environment Creation Functions ---
def create_poetry_venv():
    """Creates a virtual environment using Poetry."""
    print("\n🐍 Setting up Python environment using Poetry...")
    pyproject_path = PROJECT_DIR / "pyproject.toml"
    if not pyproject_path.exists():
        print(
            "❌ No pyproject.toml found in the new project folder. Aborting environment setup."
        )
        print(f"   Expected at: {pyproject_path}")
        print(
            "   Make sure your Cookiecutter template includes pyproject.toml in the project root."
        )
        sys.exit(1)

    ensure_poetry_installed()

    print("Installing dependencies using Poetry (this might take a while)...")
    run(["poetry", "install"])
    print("\n✅ Poetry virtual environment created and dependencies installed.")
    print("   Activate it by navigating to your project directory and running:")
    print("     poetry shell")


def create_conda_env():
    """
    Creates a Conda environment using a project's environment.yml file.
    Requires Anaconda or Miniconda to be installed and 'conda' to be in PATH.
    """
    print("\n🐍 Setting up Python environment using Conda...")
    print(
        "   (This assumes Anaconda or Miniconda is installed and 'conda' is in your PATH.)"
    )

    env_file_path = PROJECT_DIR / "environment.yml"
    if not env_file_path.exists():
        print(f"⚠️  No environment.yml found at {env_file_path}.")
        print("    Falling back to Poetry-only environment setup.")
        create_poetry_venv()
        return

    print(
        f"Creating Conda environment '{SLUG}' from {env_file_path} (this might take a while)..."
    )
    run(["conda", "env", "create", "-f", str(env_file_path), "-n", SLUG])

    print(
        f"\nInstalling Poetry-managed dependencies into Conda environment '{SLUG}'..."
    )
    print(
        "   IMPORTANT: Ensure your environment.yml file lists 'poetry' as a dependency"
    )
    print("   to make it available within the Conda environment for the next step.")
    # Ensure poetry is available globally or installed via environment.yml for this to work
    ensure_poetry_installed()  # Good to have as a fallback if not in environment.yml
    # but ideally environment.yml manages this for conda envs.

    run(["conda", "run", "-n", SLUG, "poetry", "install", "--no-venv"])

    print(f"\n✅ Conda environment '{SLUG}' created and dependencies installed.")
    print("   Activate it by running:")
    print(f"     conda activate {SLUG}")


# --- Main Execution ---
def main():
    print(f"\n🔧 Initializing environment for project: {SLUG}")

    if USE_CONDA:
        create_conda_env()
    else:
        create_poetry_venv()

    print(
        "\n💡 Optional: If your project includes a 'requirements_full.txt' for all optional dependencies,"
    )
    print("   you can install them after activating your environment by running:")
    if USE_CONDA:
        print(f"     conda run -n {SLUG} pip install -r requirements_full.txt")
    else:
        print("     poetry run pip install -r requirements_full.txt")
    print(
        "   Alternatively, use 'requirements.txt' for core/selected features (usually handled by 'poetry install')."
    )

    print("\n🎉 Project setup complete!")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        # The 'run' function now prints details, so this is a fallback.
        print(
            "\n❌ Environment setup failed due to a command error. Please review the output above."
        )
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during environment setup: {e}")
        sys.exit(1)
