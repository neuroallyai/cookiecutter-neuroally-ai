# .github/ISSUE_TEMPLATE/feature_request.md
name: "✨ Feature Request"
description: Suggest an idea, enhancement, or new feature for {{ cookiecutter.project_name }}
title: "[FEAT] A brief, descriptive title for the feature"
labels: ["enhancement", "feature request"]
# assignees: "YOUR_GITHUB_USERNAME" # Optional

body:
  - type: markdown
    attributes:
      value: |
        Thank you for your interest in improving {{ cookiecutter.project_name }}! Please describe your feature request in detail.

  - type: textarea
    id: problem-related
    attributes:
      label: "Is your feature request related to a problem or a new opportunity?"
      description: "A clear and concise description of what the problem is (e.g., 'I'm always frustrated when...') or the opportunity this feature would address."
      placeholder: "Describe the pain point or the new capability this feature would enable."
    validations:
      required: true

  - type: textarea
    id: proposed-solution
    attributes:
      label: "Describe the solution you'd like"
      description: "A clear and concise description of what you want to happen. How would this feature work?"
      placeholder: "If this feature were implemented, users could..."
    validations:
      required: true

  - type: textarea
    id: alternatives-considered
    attributes:
      label: "Describe alternatives you've considered (Optional)"
      description: "A clear and concise description of any alternative solutions or features you've considered."
    validations:
      required: false

  - type: textarea
    id: additional-context
    attributes:
      label: "Additional Context (Optional)"
      description: "Add any other context, mockups, screenshots, or links that help explain the feature request."
    validations:
      required: false

  - type: checkboxes
    id: checklist
    attributes:
      label: "Feature Request Checklist"
      description: "Before submitting, please confirm the following:"
      options:
        - label: "I have searched existing issues and discussions to ensure this feature has not already been requested."
          required: true
        - label: "I have clearly described the problem or opportunity this feature addresses."
          required: true
        - label: "I have considered the potential benefits and impact of this feature."
          required: false # User might not always know impact