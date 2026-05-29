import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.')
DATA_DIR = ROOT / 'data'

def load_json(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def safe_count(path):
    try:
        return len(load_json(path))
    except Exception:
        return 0

def count_guides():
    guide_dir = ROOT / 'guides'
    if not guide_dir.exists():
        return 0
    return sum(1 for p in guide_dir.glob('*.html'))

def main():
    generated_at = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    stats_path = DATA_DIR / 'site_stats.json'
    stats = {}
    if stats_path.exists():
        try:
            stats = load_json(stats_path)
        except Exception:
            stats = {}

    lines = [
        '# Weekly Digest',
        '',
        f'Generated: {generated_at}',
        '',
        '## Current snapshot',
        f'- Pages: {stats.get("page_count", "unknown")}',
        f'- Tools: {stats.get("tool_count", safe_count(DATA_DIR / "tools.json"))}',
        f'- Prompts: {stats.get("prompt_count", safe_count(DATA_DIR / "prompts.json"))}',
        f'- Models: {stats.get("model_count", safe_count(DATA_DIR / "models.json"))}',
        f'- Agents: {stats.get("agent_count", safe_count(DATA_DIR / "agents.json"))}',
        f'- RAG tools: {stats.get("rag_tool_count", safe_count(DATA_DIR / "rag-tools.json"))}',
        f'- Sitemap URLs: {stats.get("sitemap_url_count", "unknown")}',
        f'- Guides: {count_guides()}',
        '',
        '## Notes',
        '- This digest is generated from local project data only.',
        '- It does not include revenue, traffic, or sponsorship totals.',
    ]

    (ROOT / 'DIGEST_LATEST.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('Generated DIGEST_LATEST.md')

if __name__ == '__main__':
    main()
