# .github/ISSUE_TEMPLATE/bug_report.md
name: "🐛 Bug Report"
description: Create a report to help us improve {{ cookiecutter.project_name }}
title: "[BUG] A brief, descriptive title for the bug"
labels: ["bug", "triage"]
# assignees: "YOUR_GITHUB_USERNAME" # Optional: uncomment and set default assignee(s)

body:
  - type: markdown
    attributes:
      value: |
        Thank you for finding and reporting a bug! Please provide as much detail as possible to help us understand and reproduce the issue.

  - type: textarea
    id: description
    attributes:
      label: "Description of the Bug"
      description: "A clear and concise description of what the bug is."
      placeholder: "When I do X, then Y happens, but I expected Z."
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: "Steps To Reproduce"
      description: "Please provide detailed steps to reproduce the behavior."
      placeholder: |
        1. Go to '...'
        2. Click on '....'
        3. Observe the error '....'
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: "Expected Behavior"
      description: "A clear and concise description of what you expected to happen."
    validations:
      required: true

  - type: textarea
    id: actual-behavior
    attributes:
      label: "Actual Behavior (Optional)"
      description: "What actually happened? Include screenshots if they help illustrate the problem."
    validations:
      required: false

  - type: textarea
    id: logs
    attributes:
      label: "Error Messages & Logs"
      description: "If applicable, paste any relevant error messages, stack traces, or log output here. Please use code blocks for readability."
      render: shell
    validations:
      required: false

  - type: input
    id: project-version
    attributes:
      label: "Project Version"
      description: "What version of `{{ cookiecutter.project_name }}` are you using?"
      placeholder: "e.g., {{ cookiecutter.version }}"
    validations:
      required: true

  - type: dropdown
    id: os
    attributes:
      label: "Operating System"
      description: "What operating system are you experiencing the bug on?"
      options:
        - "Windows"
        - "macOS"
        - "Linux"
        - "Other (please specify below)"
    validations:
      required: true

  - type: input
    id: python-version
    attributes:
      label: "Python Version"
      description: "What Python version are you using? (e.g., output of `python --version`)"
      placeholder: "e.g., {{ cookiecutter.python_version }}"
    validations:
      required: true

  - type: textarea
    id: additional-context
    attributes:
      label: "Additional Context (Optional)"
      description: "Is there anything else we should know about this bug? (e.g., specific environment, browser, related issues)"
    validations:
      required: false

  - type: checkboxes
    id: checklist
    attributes:
      label: "Bug Report Checklist"
      description: "Before submitting, please confirm the following:"
      options:
        - label: "I have searched existing issues to ensure this bug has not already been reported."
          required: true
        - label: "I have provided clear steps to reproduce the issue."
          required: true
        - label: "I have included relevant version information (Project, Python, OS)."
          required: true