# {{cookiecutter.project_slug}}/src/{{cookiecutter.project_slug}}/main.py
"""
Main module for {{ cookiecutter.project_name }}.

This module can contain the primary entry point or core logic for your application.
"""

import os
from dotenv import load_dotenv

# It's good practice to load environment variables early if your app needs them
load_dotenv()

# Example: Access an environment variable
# API_KEY = os.getenv("MY_API_KEY")
# if not API_KEY:
#     print("Warning: MY_API_KEY environment variable not set.")


def greet(name: str = "World") -> str:
    """
    A simple greeting function.
    
    Args:
        name (str): The name to greet.
        
    Returns:
        str: The greeting message.
    """
    message = f"Hello, {name}, from {{ cookiecutter.project_name }}!"
    print(message)
    return message

def run_project_core_logic():
    """
    Placeholder for the main execution logic of the project.
    Replace this with your actual application's starting point.
    """
    print(f"\nRunning the core logic of {{ cookiecutter.project_name }}...")
    
    # --- TODO: Implement your project's core functionality here ---
    # For an LLM project, this might involve:
    # 1. Loading configurations (e.g., model names, API keys from .env)
    # 2. Initializing clients for LLM services (OpenAI, Gemini, Ollama, Vertex AI)
    #    (conditionally, based on {{ cookiecutter.include_X }} flags)
    # 3. Setting up a LangChain pipeline (if {{ cookiecutter.include_langchain == 'yes' }})
    # 4. Defining a sample prompt or input mechanism
    # 5. Calling the LLM and processing the response
    # 6. Displaying or saving the output
    
    greet("Developer")
    
    print("\nCore logic placeholder executed.")
    print("Edit src/{{ cookiecutter.project_slug }}/main.py to build your application.")

    # Example of conditionally using a feature
    {% if cookiecutter.include_openai == "yes" %}
    # openai_api_key = os.getenv("OPENAI_API_KEY")
    # if openai_api_key:
    #     print("OpenAI integration was selected. API key found (example).")
    #     # from openai import OpenAI
    #     # client = OpenAI() # API key is usually read from env var OPENAI_API_KEY by default
    #     # try:
    #     #     completion = client.chat.completions.create(
    #     #         model="gpt-3.5-turbo",
    #     #         messages=[{"role": "user", "content": "Say this is a test!"}]
    #     #     )
    #     #     print(f"OpenAI test response: {completion.choices[0].message.content}")
    #     # except Exception as e:
    #     #     print(f"Error calling OpenAI: {e}")
    # else:
    #     print("OpenAI integration selected, but OPENAI_API_KEY not found in .env")
    pass # Replace with actual OpenAI logic
    {% endif %}


if __name__ == "__main__":
    # This block allows the script to be run directly, for example:
    # python -m {{ cookiecutter.project_slug }}.main
    # Or, if {{ cookiecutter.project_slug }} is installed in the environment:
    # python -m {{ cookiecutter.project_slug }}
    # (if __main__.py is set up or if main.py is defined as a script in pyproject.toml)
    
    run_project_core_logic()