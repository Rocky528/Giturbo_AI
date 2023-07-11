# Giturbo GitHub App

AiCoder is a GitHub app that automates the process of creating and managing pull requests. It can create implementation plans, address PR comments, review PRs, and even implement changes based on user approval.

## Features

1. **Addressing PR Comments**: AiCoder can address feedback left on Pull Requests. It pushes to the Pull Request branch to update the PR with the requested changes.

2. **Reviewing PRs**: AiCoder can perform a code review on any pull requests. It automatically reviews the changes and leaves a comment with the result.

3. **Creating Implementation Plans**: When the 'AiCoder' label is added to an issue, GoCode creates an implementation plan. If the user approves the plan with a comment 'AiCoder', GoCode implements the necessary changes and creates a pull request.

## Usage

1. **Create an Issue**: Describe a small, unambiguous code change and reference one or more files in your codebase.

2. **Approve the Implementation Plan**: Assign the work to GoCode by adding the purple `GoCode:Gen` label. AiCoder will create an implementation plan. To approve the plan, add a comment to the Issue that starts with “LGTM”.

3. **Review the Pull Request**: AiCoder will create a new Pull Request against the default branch. If the implementation is incomplete, you can check out the branch created by GoCode and use the generated code as a starting point for your change.

## File List

1. `app.js`: The main application file.
2. `issueHandler.js`: Handles issue creation and label assignment.
3. `planCreator.js`: Creates implementation plans based on issues.
4. `prHandler.js`: Handles PR creation, review, and updates.
5. `config.js`: Contains configuration for the GitHub app.
6. `package.json`: Lists the app dependencies.
7. `README.md`: This file, contains information about the app and its usage.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

---

Please note that the file list and the file descriptions are hypothetical and should be replaced with the actual files and their descriptions used in your application.
