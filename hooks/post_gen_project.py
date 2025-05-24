import os
import subprocess
import sys
import shutil
from pathlib import Path

# 1. This is always the directory where your new project is generated!
PROJECT_DIR = Path(os.getcwd())
slug = "{{ cookiecutter.project_slug }}"
use_conda = "{{ cookiecutter.use_conda_support }}" == "yes"


def run(cmd, **kwargs):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=True, **kwargs)


def ensure_poetry():
    """Ensure Poetry is installed system-wide before continuing."""
    if shutil.which("poetry") is None:
        print("Poetry not found. Installing Poetry...")
        run("pip install --user poetry")
        print("✅ Poetry installed.")
    else:
        print("✅ Poetry already installed.")


def create_poetry_venv():
    pyproject_path = PROJECT_DIR / "pyproject.toml"
    if not pyproject_path.exists():
        print(
            "❌ No pyproject.toml found in the new project folder. Aborting environment setup."
        )
        print("   Make sure your template includes pyproject.toml in the root.")
        sys.exit(1)
    ensure_poetry()
    # Always work in the project dir
    os.chdir(PROJECT_DIR)
    run("poetry install")
    print("\n✅ Poetry venv created. Activate with:\n   poetry shell")


def create_conda_env():
    env_file = PROJECT_DIR / "environment.yml"
    if not env_file.exists():
        print("⚠️  No environment.yml found. Falling back to Poetry.")
        create_poetry_venv()
        return
    run(f"micromamba env create -f {env_file} -n {slug}")
    run(f"micromamba run -n {slug} poetry install --no-venv")
    print(
        f"\n✅ Conda env '{slug}' created. Activate with:\n   micromamba activate {slug}"
    )


def main():
    print(f"\n🔧 Setting up environment for: {slug}")
    if use_conda:
        create_conda_env()
    else:
        create_poetry_venv()
    print(
        "\n🧑‍💻 Want all optional dependencies? Run:"
        "\n   poetry run pip install -r requirements_full.txt"
        "\nOr just use requirements.txt for your selected features."
    )


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print("❌ Environment setup failed. Please run manually.")
        sys.exit(1)
