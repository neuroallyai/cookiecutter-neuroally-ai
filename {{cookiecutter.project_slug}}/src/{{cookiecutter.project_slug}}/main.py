# {{cookiecutter.project_slug}}/src/{{cookiecutter.project_slug}}/__main__.py
"""
Executable module for the {{ cookiecutter.project_name }} package.

This allows the package to be run using 'python -m {{ cookiecutter.project_slug }}'.
It typically calls the main function or entry point of the application.
"""

from .main import run_project_core_logic
# You might also import and parse command-line arguments here if not done in main.py
# import argparse


def main_cli():
    """
    Command-line entry point.
    Parses arguments (if any) and calls the main application logic.
    """
    # Example: If you were to add argument parsing:
    # parser = argparse.ArgumentParser(description="{{ cookiecutter.description }}")
    # parser.add_argument("--config", help="Path to a configuration file.")
    # args = parser.parse_args()
    #
    # run_project_core_logic(config_path=args.config)

    # For now, we'll directly call the main logic function.
    print(f"Executing {{ cookiecutter.project_name }} via __main__.py...")
    run_project_core_logic()


if __name__ == "__main__":
    main_cli()
