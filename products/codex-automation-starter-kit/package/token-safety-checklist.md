# Token Safety Checklist

Security best practices for managing API tokens, secrets, and credentials.

## Never do these

- Never commit tokens, API keys, or secrets to a Git repository
- Never paste tokens into chat messages, forums, or public channels
- Never share tokens via email or messaging apps
- Never store tokens in plain text files committed to Git
- Never use git push --force on shared branches
- Never run untrusted scripts without reading them first

## Always do these

- Use environment variables for secrets in local development
- Use GitHub repository secrets for CI/CD tokens
- Use .gitignore to exclude .env and other secret files
- Rotate tokens regularly (at least every 90 days)
- Use the principle of least privilege (minimum required permissions)
- Review repository access periodically

## .gitignore template

Always include these in your .gitignore:

```
__pycache__/
*.pyc
.env
.env.local
.env.*.local
.DS_Store
Thumbs.db
node_modules/
dist/
*.log
```

## GitHub token setup

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Create a fine-grained token with only the required permissions
3. For repository automation, use contents: read and contents: write
4. Store the token as a GitHub repository secret (Settings > Secrets)
5. Reference it in workflows as ${{ secrets.YOUR_SECRET_NAME }}

## Environment variable setup (Windows PowerShell)

```powershell
# Set for current session only
$env:MY_API_KEY = "your-key-here"

# Set permanently for current user
[System.Environment]::SetEnvironmentVariable("MY_API_KEY", "your-key-here", "User")

# Read an environment variable
$env:MY_API_KEY
```

## What to do if a token is leaked

1. Immediately revoke the exposed token on the provider website
2. Generate a new token with the same or fewer permissions
3. Update all places where the old token was used (local env, GitHub secrets)
4. Check repository git history for other potential leaks
5. If the token is in git history, consider using BFG Repo-Cleaner (requires force push)

## Checklist

- [ ] .gitignore includes .env, *.pyc, __pycache__/
- [ ] No tokens in any committed files (check with grep)
- [ ] GitHub secrets configured for CI/CD
- [ ] Tokens have minimal required permissions
- [ ] Token rotation schedule set (90 days recommended)
