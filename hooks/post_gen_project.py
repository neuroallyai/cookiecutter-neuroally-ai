import os
import subprocess
import sys
from pathlib import Path

# These come in as Jinja strings. You'll need to copy-paste all your variables here:
slug = "{{ cookiecutter.project_slug }}"
use_conda = "{{ cookiecutter.use_conda_support }}" == "yes"

# Flatten your nested advanced options
include_streamlit = (
    "{{ cookiecutter._advanced_options['UI Frameworks']['include_streamlit'] }}"
    == "yes"
)
include_fastapi = (
    "{{ cookiecutter._advanced_options['UI Frameworks']['include_fastapi'] }}" == "yes"
)
include_langchain = (
    "{{ cookiecutter._advanced_options['LLM Integrations']['include_langchain'] }}"
    == "yes"
)
include_openai = (
    "{{ cookiecutter._advanced_options['LLM Integrations']['include_openai'] }}"
    == "yes"
)
# ...repeat for each nested option you want to use

PROJECT_DIR = Path(__file__).resolve().parent.parent


def run(cmd, **kwargs):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=True, **kwargs)


def create_poetry_venv():
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
    # Example: run something extra only if Streamlit or OpenAI was selected
    if include_streamlit:
        print("🚀 Streamlit UI enabled.")
    if include_openai:
        print("🤖 OpenAI integration enabled.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print("❌ Environment setup failed. Please run manually.")
        sys.exit(1)
