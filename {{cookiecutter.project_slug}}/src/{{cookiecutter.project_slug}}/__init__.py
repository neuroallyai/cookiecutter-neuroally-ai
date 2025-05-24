# {{cookiecutter.project_slug}}/src/{{cookiecutter.project_slug}}/__init__.py
"""
{{ cookiecutter.project_name }}

{{ cookiecutter.description }}

This is the main package for {{ cookiecutter.project_name }}.
You can import its core functionalities from here. For example:

   from {{ cookiecutter.project_slug }} import main_function
   main_function()

(Update this docstring as you develop your package's API.)
"""

# Define the package version.
# This version should ideally be sourced from a single place, often pyproject.toml.
# For simplicity in this scaffold, we'll use the version from cookiecutter.json.
# Tools like `poetry-dynamic-versioning` or reading pyproject.toml at runtime
# (e.g., with `importlib.metadata`) are more advanced ways to manage this.
__version__ = "{{ cookiecutter.version }}"  # From cookiecutter.json

# Expose key functionalities from your submodules here for easier access.
# For example, if you have a function `run_analysis` in `main.py`:
# from .main import run_analysis
#
# This allows users to do:
# import {{ cookiecutter.project_slug }}
# {{ cookiecutter.project_slug }}.run_analysis()
#
# Or, for more selective imports if using `from {{ cookiecutter.project_slug }} import *`:
# __all__ = ['run_analysis']


# For a new scaffold, you might not have much to export yet.
# Add your main functions/classes here as your package develops.
print(
    f"Package '{{ cookiecutter.project_slug }}' version {__version__} loaded."
)  # Optional: for debug or confirmation
