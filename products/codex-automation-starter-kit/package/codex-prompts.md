# Codex Prompts

Ready-to-use prompts for common Codex CLI tasks. Adapt these to your specific project.

## Project analysis

### List and analyze project structure
```
List all files in the current directory recursively. Show the directory tree structure. Identify the main languages and frameworks used. Suggest improvements to the project organization.
```

### Audit existing codebase
```
Review the current project structure. Identify: 1) Missing files that should exist (README, .gitignore, LICENSE), 2) Files that should not be committed (secrets, caches), 3) Suggested directory structure improvements. Output a markdown audit report.
```

## Data and content

### Create structured data files
```
Create a data/ directory with a tools.json file containing AI tool entries. Each tool should have: name, url, category, pricing, description, tags, and last_checked fields. Start with 5 example entries.
```

### Generate pages from data
```
Create a Python script scripts/build_site.py that reads data/tools.json and generates static HTML pages. Requirements: dark theme, responsive, include title and meta description, link to Ko-fi for support. Output to the current directory.
```

## Automation

### Create build and deploy workflow
```
Create .github/workflows/build-site.yml that: 1) Triggers on push to main, 2) Sets up Python 3.12, 3) Runs scripts/build_site.py, 4) Uploads artifact, 5) Deploys to GitHub Pages. Use official GitHub actions only.
```

### Create weekly refresh workflow
```
Create .github/workflows/seo-refresh.yml that: 1) Runs weekly on Monday, 2) Regenerates pages and sitemap, 3) Commits changes with [skip ci] in the message, 4) Only commits if there are actual changes (git status --porcelain).
```

## Safety and quality

### Scan for secrets
```
Scan all files in the repository for potential secrets, API keys, tokens, or passwords. Check for patterns like: sk-*, ghp_*, Bearer tokens, hardcoded passwords. Report findings and suggest how to fix each one.
```

### Validate links
```
Create scripts/check_links.py that: 1) Scans all .html files for href attributes, 2) Checks local links resolve to existing files, 3) Reports broken links with file and line number, 4) Ignores template placeholders like ${{...}}.
```

### Generate sitemap
```
Create scripts/update_sitemap.py that: 1) Scans all .html files, 2) Generates sitemap.xml with correct URLs, 3) Uses file modification time for lastmod, 4) Excludes .git and __pycache__ directories.
```
