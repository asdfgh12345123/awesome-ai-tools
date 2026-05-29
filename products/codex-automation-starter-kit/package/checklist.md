# Project Organization Checklist

Use this checklist to prepare your project for AI-assisted automation with Codex and GitHub Actions.

## Repository structure

- [ ] Project has a clear README.md with description and setup instructions
- [ ] scripts/ directory exists for automation scripts
- [ ] data/ directory exists for structured data files (JSON, CSV)
- [ ] .gitignore is configured (ignore __pycache__/, *.pyc, .env, node_modules/)
- [ ] No secrets or tokens committed to the repository
- [ ] LICENSE file exists if the project is public

## GitHub setup

- [ ] Repository is public (or private with appropriate access)
- [ ] GitHub Actions are enabled in repository settings
- [ ] FUNDING.yml is configured if you want sponsorship buttons
- [ ] Branch protection rules are set (recommended for main branch)
- [ ] Repository description and topics are filled in

## Local environment

- [ ] Git is installed and configured (git config user.name, git config user.email)
- [ ] Python 3.10+ is installed and in PATH
- [ ] GitHub CLI (gh) is installed for authentication
- [ ] Codex CLI is installed (npm install -g @openai/codex)
- [ ] A code editor is installed (VS Code recommended)

## Security

- [ ] Review token-safety-checklist.md before adding any tokens
- [ ] Use environment variables for secrets, never hardcode them
- [ ] Use GitHub repository secrets for CI/CD tokens
- [ ] .env is in .gitignore
- [ ] No API keys in any committed files

## First automation

- [ ] Create a build script (e.g., scripts/build_site.py) that generates or updates content
- [ ] Create a GitHub Actions workflow (.github/workflows/build-site.yml)
- [ ] Test the workflow by pushing to the repository
- [ ] Verify the output on GitHub Pages or your hosting platform
- [ ] Add a weekly refresh workflow with [skip ci] in the commit message
