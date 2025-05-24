import os
import subprocess
import sys
from pathlib import Path
import shutil

PROJECT_DIR = Path(__file__).resolve().parent.parent
slug = "{{ cookiecutter.project_slug }}"
use_conda = "{{ cookiecutter.use_conda_support }}" == "yes"


def run(cmd, **kwargs):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=True, **kwargs)


def ensure_poetry():
    """Ensure poetry is installed system-wide before continuing."""
    if shutil.which("poetry") is None:
        print("Poetry not found. Installing Poetry...")
        run("pip install --user poetry")
        print("✅ Poetry installed.")
    else:
        print("✅ Poetry already installed.")


def create_poetry_venv():
    ensure_poetry()
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
    os.chdir(PROJECT_DIR)
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
