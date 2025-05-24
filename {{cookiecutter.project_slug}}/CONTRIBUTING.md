{{cookiecutter.project_slug}}/CONTRIBUTING.md (Template):

Markdown

# Contributing to {{ cookiecutter.project_name }}

We love seeing contributions from the community and are excited to welcome yours! Whether you're fixing a bug, improving documentation, or proposing a new feature, your help is valued.

Thank you for your interest in making {{ cookiecutter.project_name }} better!

## Table of Contents
- [Contributing to {{ cookiecutter.project\_name }}](#contributing-to--cookiecutterproject_name-)
  - [Table of Contents](#table-of-contents)
  - [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Your First Code Contribution](#your-first-code-contribution)
    - [Pull Requests](#pull-requests)
  - [Development Setup](#development-setup)

## How Can I Contribute?

### Reporting Bugs
If you encounter a bug, please help us by reporting it! Before creating a bug report, please check existing issues to see if someone has already reported it.

When creating a bug report, please include:
- A clear and descriptive title.
- Steps to reproduce the bug.
- What you expected to happen.
- What actually happened (including any error messages or tracebacks).
- Your environment details (e.g., OS, Python version `{{ cookiecutter.python_version }}`, version of {{ cookiecutter.project_name }} `{{ cookiecutter.version }}`, browser if applicable).

### Suggesting Enhancements
We're always open to suggestions for new features or improvements to existing functionality.
- Clearly describe the enhancement and the problem it solves.
- Explain the benefits this enhancement would bring to users.
- If possible, provide examples or mockups of how it might work.

### Your First Code Contribution
Unsure where to begin contributing to {{ cookiecutter.project_name }}?
- Look for issues tagged `good first issue` or `help wanted`.
- You can also start by improving documentation or adding more tests.

### Pull Requests
1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/issue-number-description`.
3. Make your changes. Ensure you add or update tests as appropriate.
4. Ensure your code lints and tests pass (e.g., `make lint` and `make test` if a Makefile is provided, or run the commands manually).
5. Commit your changes with a clear and descriptive commit message.
6. Push your branch to your fork: `git push origin feature/your-feature-name`.
7. Open a pull request to the `main` (or `develop`) branch of the original repository.
8. Clearly describe your changes in the pull request. Link to any relevant issues.

## Development Setup

To set up your development environment for {{ cookiecutter.project_name }}, please follow the instructions in the main [README.md](./README.md) under the "Getting Started" section. This will guide you through setting up {% if cookiecutter.use_conda_support == "yes" %}Conda and Poetry{% else %}Poetry{% endif %}, and installing core and development dependencies.

It's recommended to install development tools using:
```bash
{% if cookiecutter.use_conda_support == "yes" -%}
conda run -n {{ cookiecutter.project_slug }} poetry install --with dev
{%- else -%}
poetry install --with dev
{%- endif %}
This will install tools like pytest for testing, and linters/formatters if configured in the dev group of pyproject.toml.

Coding Standards
TODO: Define any specific coding standards or style guides (e.g., "We follow PEP 8 strictly," "Use Black for code formatting," "Docstrings should follow X format").
Ensure your code is well-commented where necessary.
Write clear and concise commit messages.
{% if cookiecutter.include_code_of_conduct == "yes" %}

Code of Conduct
This project and everyone participating in it is governed by the {{ cookiecutter.project_name }} Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior.
{% else %}

Code of Conduct
We expect all contributors to interact respectfully and constructively. (TODO: Consider adding a formal Code of Conduct).
{% endif %}

Questions?
If you have any questions about contributing, feel free to open an issue or reach out to {{ cookiecutter.author_name }} at {{ cookiecutter.author_email }}.

Thank you for contributing!


**Key aspects of this `CONTRIBUTING.md` template:**

* **Conditional Generation:** The file itself will only be created if `{{ cookiecutter.include_contributing == 'yes' }}`.
* **Dynamic Information:** Uses `{{ cookiecutter.project_name }}`, `{{ cookiecutter.python_version }}`, `{{ cookiecutter.version }}`, `{{ cookiecutter.author_name }}`, `{{ cookiecutter.author_email }}`, and `{{ cookiecutter.project_slug }}`.
* **Standard Sections:** Covers how to report bugs, suggest features, make pull requests, setup development environment, and coding standards (with TODOs for specifics).
* **Links to Other Files:** Dynamically links to `README.md` and conditionally to `CODE_OF_CONDUCT.md`.
* **Makefile Reference:** Suggests using `make` targets if available.
* **Poetry/Conda Commands:** Provides correct commands for installing dev dependencies.

**Action for you:**

1.  **Create the conditional file** in your template:
    `cookiecutter-neuroally-ai/{{cookiecutter.project_slug}}/{% if cookiecutter.include_contributing == 'yes' %}CONTRIBUTING.md{% endif %}`
2.  **Paste the content above** into this file.
3.  Remember to fill in the `TODO:` sections within the template or add comments guiding the end-user on what to fill in their generated project.

---

After this, we can similarly define `CODE_OF_CONDUCT.md` and `SECURITY.md`. Ready to proceed with `CODE_OF_CONDUCT.md` next?