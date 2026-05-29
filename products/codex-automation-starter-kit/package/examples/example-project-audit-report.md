# Example: Project Audit Report

This is an example of what Codex can produce when asked to audit a project structure.

## Prompt used

```
Review the current project structure. Identify: 1) Missing files that should exist (README, .gitignore, LICENSE), 2) Files that should not be committed (secrets, caches), 3) Suggested directory structure improvements. Output a markdown audit report.
```

## Example output

# Project Audit Report

**Project**: my-ai-tools-site
**Date**: 2026-05-29
**Auditor**: Codex CLI

## Current structure

```
my-ai-tools-site/
  index.html
  tools.html
  .env              <-- PROBLEM
  __pycache__/      <-- PROBLEM
  scripts/
    build.py
```

## Issues found

### Critical

1. **.env is committed** - This file likely contains API keys or secrets. Remove from git history and add to .gitignore.
2. **__pycache__/ is committed** - Python bytecode should not be in version control.

### Missing files

1. **README.md** - No project description or setup instructions
2. **.gitignore** - No ignore rules configured
3. **LICENSE** - No license file for public repository

### Suggestions

1. Create a `data/` directory for structured content (JSON files)
2. Move build output to a `dist/` or `_site/` directory
3. Add a `scripts/generate_sitemap.py` for SEO

## Recommended actions

1. Create .gitignore with: __pycache__/, *.pyc, .env, .DS_Store
2. Remove .env from git: `git rm --cached .env`
3. Create README.md with project description
4. Add LICENSE file (MIT or Apache 2.0 recommended)
5. Reorganize scripts into build, generate, and check categories
