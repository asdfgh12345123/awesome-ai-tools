# Codex Prompts

Ready-to-use prompts for common Codex CLI tasks. Adapt these to your specific project.

## Project structure

### Analyze project structure
\List all files in the current directory recursively. Show the directory tree structure. Identify the main languages and frameworks used.
\
### Create data files
\Create a data/ directory with a tools.json file. Each tool should have: name, url, category, pricing, description, tags, and last_checked fields.
\
### Generate pages from data
\Create a Python script scripts/build_site.py that reads data/tools.json and generates HTML pages. Each page should have a title, meta description, and a clean dark theme.
\
## Automation

### Create GitHub Actions workflow
\Create a .github/workflows/build-site.yml that:
1. Triggers on push to main
2. Sets up Python 3.12
3. Runs scripts/build_site.py
4. Deploys the output to GitHub Pages
\
### Update sitemap
\Create a Python script scripts/update_sitemap.py that scans all .html files and generates a sitemap.xml with the correct URLs.
\
## Content

### Add a new tool entry
\Add a new entry to data/tools.json with the following information:
- name: [Tool Name]
- url: [Official URL]
- category: [Category]
- pricing: [Free/Freemium/Paid/Unknown]
- description: [Brief description]
\
### Generate guide pages
\Create a Python script scripts/generate_guides.py that reads data/ files and generates guide HTML pages with comparison tables and FAQ sections.
\
## Safety

### Check for secrets
\Scan all files in the repository for potential secrets, API keys, or tokens. Report any findings and suggest how to move them to environment variables.
\
### Validate links
\Create a Python script scripts/check_links.py that checks all local links in HTML files and reports broken links.
\