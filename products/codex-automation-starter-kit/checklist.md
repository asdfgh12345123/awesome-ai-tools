# Project Organization Checklist

Use this checklist to prepare your project for AI-assisted automation with Codex and GitHub Actions.

## Repository structure

- [ ] Project has a clear README.md with description and setup instructions
- [ ] scripts/ directory exists for automation scripts
- [ ] data/ directory exists for structured data files (JSON, CSV)
- [ ] .gitignore is configured (ignore __pycache__/, *.pyc, .env, node_modules/)
- [ ] No secrets or tokens committed to the repository

## GitHub setup

- [ ] Repository is public (or private with appropriate access)
- [ ] GitHub Actions are enabled in repository settings
- [ ] FUNDING.yml is configured if you want sponsorship buttons
- [ ] Branch protection rules are set if needed

## Local environment

- [ ] Git is installed and configured
- [ ] Python 3.10+ is installed
- [ ] GitHub CLI (gh) is installed for authentication
- [ ] Codex CLI is installed (npm install -g @openai/codex)

## Security

- [ ] Review token-safety-checklist.md before adding any tokens
- [ ] Use environment variables for secrets, never hardcode them
- [ ] Use GitHub repository secrets for CI/CD tokens
- [ ] Regularly rotate tokens and review access

## Automation

- [ ] Create a build script that generates or updates content
- [ ] Create a GitHub Actions workflow that runs the build script
- [ ] Test the workflow by pushing to the repository
- [ ] Verify the output on GitHub Pages or your hosting platform
