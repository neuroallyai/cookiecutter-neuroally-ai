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
PROJECT_NAME = "{{ cookiecutter.project_name }}"  # Added for commit message

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
        subprocess.run(
            command_args, shell=is_shell_command, check=True, cwd=PROJECT_DIR, **kwargs
        )
    except FileNotFoundError as e:
        cmd_name = command_args if is_shell_command else command_args[0]
        print(
            f"❌ Error: Command '{cmd_name}' not found. Please ensure it's installed and in your PATH."
        )
        print(f"   Details: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd_display_str}")
        print(f"   Return code: {e.returncode}")
        if e.stdout and e.stdout.strip():  # Only print if there's actual output
            print(f"   Stdout: {e.stdout.decode(errors='ignore').strip()}")
        if e.stderr and e.stderr.strip():  # Only print if there's actual output
            print(f"   Stderr: {e.stderr.decode(errors='ignore').strip()}")
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
            print(
                "✅ Poetry installed via pip. Please ensure your PATH is configured correctly."
            )
            print(
                "   You might need to open a new terminal session for 'poetry' to be available."
            )
            if shutil.which("poetry") is None:  # Re-check after install attempt
                print(
                    "   WARNING: Poetry still not found in PATH after pip install --user."
                )
                print(
                    "            Please verify your PATH or install Poetry using the official installer."
                )
                print(
                    "            Skipping further Poetry-dependent steps in this script if any."
                )
                return False  # Indicate poetry is not ready
        except Exception as e:
            print("❌ Failed to install Poetry using pip.")
            print(
                "   Please install Poetry manually: https://python-poetry.org/docs/#installation"
            )
            sys.exit(1)
    else:
        print("✅ Poetry already installed.")
    return True  # Indicate poetry is ready


def initialize_git_repo():
    """Initializes a Git repository in the project directory."""
    if shutil.which("git") is None:
        print("\n⚠️ Git not found. Skipping Git repository initialization.")
        print(
            "   Please install Git if you want to use version control: https://git-scm.com/downloads"
        )
        return

    if (PROJECT_DIR / ".git").exists():
        print("\n✨ Git repository already initialized.")
        return

    print("\n✨ Initializing Git repository...")
    try:
        run(["git", "init"])
        run(["git", "add", "."])  # Stage all generated files
        commit_message = (
            f"feat: Initial commit for {PROJECT_NAME} from Cookiecutter template"
        )
        # Allow commit to fail if git user not configured, but don't stop script
        try:
            run(["git", "commit", "-m", commit_message])
            print("✅ Git repository initialized and initial commit made.")
        except subprocess.CalledProcessError as e:
            print(
                f"⚠️  Could not make initial commit (git user/email may not be configured): {e}"
            )
            print(
                "   Please run 'git commit' manually after configuring git if needed."
            )

        print("\n   Next steps for Git:")
        print("   1. Create a remote repository (e.g., on GitHub, GitLab).")
        print("   2. Add the remote: git remote add origin YOUR_REMOTE_REPOSITORY_URL")
        print(
            "   3. Push your initial commit: git push -u origin main (or your default branch name)"
        )
    except Exception as e:
        print(f"⚠️ Failed to initialize Git repository: {e}")
        print("   Please run 'git init' manually if desired.")


# --- Environment Creation Functions ---
def create_poetry_venv():
    """Creates a virtual environment and installs core dependencies using Poetry."""
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

    if not ensure_poetry_installed():
        print("   Skipping Poetry dependency installation as Poetry is not available.")
        return

    print("Installing core dependencies using Poetry (this might take a while)...")
    run(["poetry", "install"])  # This installs main and default dev dependencies
    print("\n✅ Poetry virtual environment created and core dependencies installed.")
    print("   Activate it by navigating to your project directory and running:")
    print("     poetry shell")


def create_conda_env():
    """
    Creates a Conda environment and installs core dependencies using Poetry within Conda.
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
    run(
        ["conda", "env", "create", "-f", str(env_file_path), "-n", SLUG, "--force"]
    )  # Added --force to overwrite if exists

    print(
        f"\nInstalling core Poetry-managed dependencies into Conda environment '{SLUG}'..."
    )
    print(
        "   IMPORTANT: Ensure your environment.yml file lists 'poetry' as a dependency"
    )
    print("   to make it available within the Conda environment for the next step.")

    # Check if Poetry is callable within the Conda environment context before trying to use it
    # ensure_poetry_installed() here would check/install global/user poetry, which might not be
    # the one used by `conda run`. It's better to rely on environment.yml to provide Poetry.
    # If environment.yml doesn't provide poetry, the `conda run poetry` command might fail.
    # The user will then see the error and know to fix environment.yml or ensure poetry is in PATH.

    run(
        ["conda", "run", "-n", SLUG, "poetry", "install"]
    )  # Installs main and default dev dependencies

    print(f"\n✅ Conda environment '{SLUG}' created and core dependencies installed.")
    print("   Activate it by running:")
    print(f"     conda activate {SLUG}")


# --- Main Execution ---
def main():
    print(f"\n🚀 Starting project setup for: {PROJECT_NAME} ({SLUG})")

    initialize_git_repo()  # Initialize Git repository first

    print(f"\n🔧 Setting up Python environment...")
    if USE_CONDA:
        create_conda_env()
    else:
        create_poetry_venv()

    print("\n💡 Next Steps & Optional Features:")
    print("   Your project is set up with core dependencies.")
    print(
        "   For optional features you may have selected during generation (e.g., FastAPI, Langchain, etc.),"
    )
    print(
        "   please refer to the 'Installing Optional Features' section in your project's README.md."
    )
    print(
        "   This will guide you on how to install them using Poetry's dependency groups"
    )
    print("   (e.g., 'poetry install --with <feature_group>' or equivalent for Conda).")

    print("\n🎉 Project setup complete!")
    print(f"   Navigate to your project directory: cd {SLUG}")
    print("   Then activate your environment and start developing!")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print(
            "\n❌ Environment setup failed due to a command error. Please review the output above."
        )
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during environment setup: {e}")
        import traceback

        traceback.print_exc()  # Print full traceback for unexpected errors
        sys.exit(1)
