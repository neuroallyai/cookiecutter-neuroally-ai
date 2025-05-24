t's good practice to include a README.md inside the notebooks directory to guide users.

Path in template: cookiecutter-neuroally-ai/{{cookiecutter.project_slug}}/{% if cookiecutter.include_notebooks == 'yes' %}notebooks{% endif %}/README.md

Content:

Markdown

# Notebooks for {{ cookiecutter.project_name }}

This directory contains Jupyter notebooks for various purposes such as:
- Data exploration and analysis
- Model experimentation and prototyping
- Visualizations
- Interactive examples and tutorials

## Naming Convention

It's recommended to follow a consistent naming convention for notebooks to keep them organized. For example:

- `01-initial-data-exploration.ipynb`
- `02-feature-engineering-ideas.ipynb`
- `exp001-model-alpha-tuning.ipynb`
- `{{ cookiecutter.author_name | lower | replace(' ', '')[:3] }}-<short-description>.ipynb` (e.g., `jsc-text-summarization-test.ipynb`)

Choose a convention that works best for your team and project.

## Kernel Setup

To ensure notebooks use the project's Python environment (managed by Poetry or Conda), you should configure a Jupyter kernel that points to it. The `notebooks` dependency group in `pyproject.toml` (which includes `jupyterlab` and `ipykernel`) should be installed first (`poetry install --with notebooks`).

**1. Activate your project environment:**
{% if cookiecutter.use_conda_support == "yes" -%}
```bash
conda activate {{ cookiecutter.project_slug }}
{%- else -%}

Bash

poetry shell
{%- endif %}

2. Register the environment as a Jupyter kernel (run from within the activated environment):

Bash

python -m ipykernel install --user --name="{{ cookiecutter.project_slug }}" --display-name "Python ({{ cookiecutter.project_slug }})"
3. Using the kernel:
After registering, when you open JupyterLab or Jupyter Notebook (launched from your activated environment or globally), you should be able to select the kernel named Python ({{ cookiecutter.project_slug }}) (or similar) for your notebooks.

Alternatively, simply launching jupyter lab or jupyter notebook from within your activated project environment (after jupyterlab and ipykernel are installed in it) should often make the correct kernel available by default or as a clear option.

Best Practices
Keep notebooks focused on a specific task or exploration.
Document your steps and findings within the notebooks using Markdown cells.
Consider versioning "cleared" versions of notebooks (outputs stripped) if output cells are large or change frequently. Tools like nbstripout can automate this as a Git filter.
For reproducible pipelines and core logic, refactor useful code from notebooks into Python scripts in the src/{{ cookiecutter.project_slug }}/ directory.
