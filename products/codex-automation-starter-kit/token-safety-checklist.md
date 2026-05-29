# Token Safety Checklist

Security best practices for managing API tokens, secrets, and credentials.

## Never do these

- Never commit tokens, API keys, or secrets to a Git repository
- Never paste tokens into chat messages or public forums
- Never share tokens via email or messaging apps
- Never store tokens in plain text files committed to Git
- Never use git push --force on shared branches

## Always do these

- Use environment variables for secrets in local development
- Use GitHub repository secrets for CI/CD tokens
- Use .gitignore to exclude .env and other secret files
- Rotate tokens regularly (at least every 90 days)
- Use the principle of least privilege (minimum required permissions)

## GitHub token setup

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Create a fine-grained token with only the required permissions
3. For repository automation, use contents: read and contents: write
4. Store the token as a GitHub repository secret
5. Reference it in workflows as ${{ secrets.YOUR_SECRET_NAME }}

## .gitignore template

~~~
__pycache__/
*.pyc
.env
.env.local
.DS_Store
Thumbs.db
node_modules/
~~~

## What to do if a token is leaked

1. Immediately revoke the exposed token on the provider website
2. Generate a new token with the same or fewer permissions
3. Update all places where the old token was used
4. Check repository history for other potential leaks
