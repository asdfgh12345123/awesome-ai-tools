# Example: Codex Handoff Prompt

Use this type of prompt when starting a new Codex session to give it context about your project.

## The prompt

```
You are working on a static website project called "AI Tools Hub".

Project path: C:\Users\me\projects\ai-tools-hub

Current state:
- The site has 15 HTML pages generated from data/tools.json
- Build script: scripts/build_site.py (Python 3.12)
- Sitemap generator: scripts/update_sitemap.py
- Link checker: scripts/check_links.py
- All pages use a dark theme with system-ui font
- Site is deployed to GitHub Pages via .github/workflows/build-site.yml

What I need:
- Add a new data file data/prompts.json with ChatGPT prompt examples
- Update build_site.py to generate a prompts page from the new data
- Run all scripts to verify everything works
- Commit and push if successful

Rules:
- Do not commit .env, __pycache__, or any secrets
- Do not use git push --force
- Do not delete existing pages
- If a script fails, report the error and stop (do not guess fixes)
```

## Why this works

1. **Context**: Tells Codex what the project is, where it lives, and what tools exist
2. **Current state**: Summarizes what already works so Codex does not redo it
3. **Clear task**: Specific, bounded request with clear success criteria
4. **Safety rules**: Prevents common mistakes

## Tips

- Be specific about file paths and tool versions
- List what already works so Codex does not break it
- Include safety rules to prevent destructive actions
- If the task is complex, break it into numbered steps
