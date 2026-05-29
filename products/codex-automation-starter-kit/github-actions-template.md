# GitHub Actions Template

A minimal GitHub Actions workflow for static site generation and deployment.

## Build and Deploy

~~~yaml
name: Build Site

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12
      - name: Build pages
        run: python scripts/build_site.py
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
~~~

## Weekly Refresh

~~~yaml
name: SEO Refresh

on:
  schedule:
    - cron: 30 1 * * 1
  workflow_dispatch:

permissions:
  contents: write

jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12
      - name: Regenerate pages
        run: python scripts/build_site.py && python scripts/update_sitemap.py
~~~

## Usage

1. Copy the YAML content into .github/workflows/ in your repository
2. Adjust the Python script paths to match your project
3. Push to main to trigger the first build
4. Check the Actions tab in your repository for build status