# Windows Commands Reference

Common PowerShell and Git commands for project automation on Windows.

## Git basics

```powershell
# Initialize a repository
git init

# Check status
git status

# Stage all changes
git add .

# Commit
git commit -m "your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Check remote configuration
git remote -v

# Set remote URL
git remote set-url origin https://github.com/username/repo.git
```

## Python scripts

```powershell
# Run a Python script
python scripts/build_site.py

# Check Python version
python --version

# Validate Python syntax without running
python -m py_compile scripts/build_site.py

# Run multiple scripts in sequence
python scripts/build_site.py; python scripts/update_sitemap.py
```

## GitHub CLI

```powershell
# Check authentication status
gh auth status

# Login to GitHub (opens browser)
gh auth login

# Setup git credentials from gh
gh auth setup-git

# View repository info
gh repo view username/repo
```

## File operations

```powershell
# List files recursively
Get-ChildItem -Recurse -Filter *.html

# Search for text in files
Get-ChildItem -Recurse -Filter *.py | Select-String -Pattern "import"

# Check file content
Get-Content data/tools.json

# Count files by extension
Get-ChildItem -Recurse -File | Group-Object Extension | Sort-Object Count -Descending
```

## Credential management

```powershell
# Clear cached GitHub credentials
@"
protocol=https
host=github.com
"@ | git credential reject

# Check Git configuration
git config --list

# Set local Git config (per-repo only)
git config user.name "Your Name"
git config user.email "your@email.com"

# Set credential helper
git config --global credential.helper manager
```

## DANGEROUS COMMANDS - Use with caution

```powershell
# [DANGER] Force push - overwrites remote history
# Only use on personal branches, never on shared branches
# git push --force origin main

# [DANGER] Reset to remote - loses all local changes
# git reset --hard origin/main

# [DANGER] Clean untracked files - permanently deletes
# git clean -fd

# [DANGER] Delete branch
# git branch -d branch-name
```
