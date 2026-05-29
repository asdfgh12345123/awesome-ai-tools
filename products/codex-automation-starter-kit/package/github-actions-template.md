# GitHub Actions Templates

Starter YAML workflows for static site generation and deployment. Copy these into .github/workflows/ in your repository.

## Build and Deploy (build-site.yml)

This workflow builds your site and deploys to GitHub Pages on every push to main.

```yaml
name: Build Site

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Build pages
        run: python scripts/build_site.py

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Weekly SEO Refresh (seo-refresh.yml)

This workflow regenerates content weekly and commits changes with [skip ci] to avoid infinite loops.

```yaml
name: SEO Refresh

on:
  schedule:
    - cron: '30 1 * * 1'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  refresh-generated-content:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Regenerate pages and stats
        run: |
          python scripts/build_site.py
          python scripts/update_sitemap.py
          python scripts/generate_stats.py

      - name: Run link check
        run: python scripts/check_links.py

      - name: Commit updated assets if changed
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            git config user.name "github-actions[bot]"
            git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
            git add .
            git commit -m "chore: refresh generated site data [skip ci]"
            git push
          else
            echo "No changes to commit"
          fi
```

## Link Check (link-check.yml)

This workflow checks for broken links weekly without making any changes.

```yaml
name: Link Check

on:
  schedule:
    - cron: '15 1 * * 1'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run local link check
        run: python scripts/check_links.py
```

## Important notes

- Always use [skip ci] in auto-commit messages to prevent infinite loops
- Use minimal permissions (contents: read for build, contents: write for refresh)
- Use official GitHub actions (actions/checkout, actions/setup-python, etc.)
- Never commit tokens or secrets in workflow files
