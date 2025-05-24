# {{cookiecutter.project_slug}}/tests/test_example.py
"""
Example test module for {{ cookiecutter.project_name }}.

This module contains basic example tests using pytest.
"""

import pytest
from {{ cookiecutter.project_slug }} import main  # Assuming your main logic/functions are in 'main.py'
from {{ cookiecutter.project_slug }} import __version__ as project_version

def test_project_version():
    """Test that the project version is accessible and a string."""
    assert isinstance(project_version, str)
    # You could add a more specific version check if desired, e.g., matching pyproject.toml
    # For now, just checking it's a string is a good start.
    print(f"Project version from __init__.py: {project_version}") # Optional: for visibility during test run
    assert project_version == "{{ cookiecutter.version }}" # Check against cookiecutter.json version

def test_greet_default():
    """Test the greet function with default arguments."""
    expected_greeting = f"Hello, World, from {{ cookiecutter.project_name }}!"
    assert main.greet() == expected_greeting

def test_greet_with_name():
    """Test the greet function with a specific name."""
    name_to_greet = "Developer"
    expected_greeting = f"Hello, {name_to_greet}, from {{ cookiecutter.project_name }}!"
    assert main.greet(name_to_greet) == expected_greeting

# Example of a test that might be skipped if a condition isn't met
# (e.g., an API key isn't available for an integration test)
# import os
# @pytest.mark.skipif(not os.getenv("SOME_API_KEY"), reason="SOME_API_KEY not set in environment")
# def test_api_dependent_feature():
#     """Example of a test for a feature that requires an API key."""
#     # ... your test logic that uses SOME_API_KEY ...
#     assert True # Replace with actual assertion

# You can add more tests here for other functionalities.
# Consider organizing tests into multiple files as your test suite grows.
# For example:
#   test_module_x.py
#   test_integration_y.py

# To run tests (assuming pytest is installed via the 'dev' group):
# poetry run pytest
# or if using Conda:
# conda run -n {{ cookiecutter.project_slug }} pytest