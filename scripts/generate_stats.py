#!/usr/bin/env python3
import json, os
from datetime import datetime

DATA_DIR = 'data'
OUTPUT_JSON = os.path.join(DATA_DIR, 'site_stats.json')

def count_html():
    n = 0
    for root, dirs, files in os.walk('.'):
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith('.html'):
                n += 1
    return n

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def main():
    tools = load_json('tools.json')
    prompts = load_json('prompts.json')
    models = load_json('models.json')
    agents = load_json('agents.json')
    rag = load_json('rag-tools.json')
    pages = count_html()
    sitemap_urls = 0
    if os.path.exists('sitemap.xml'):
        with open('sitemap.xml', 'r', encoding='utf-8') as f:
            sitemap_urls = f.read().count('<url>')
    stats = {
        'generated_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'page_count': pages,
        'tool_count': len(tools),
        'prompt_count': len(prompts),
        'model_count': len(models),
        'agent_count': len(agents),
        'rag_tool_count': len(rag),
        'sitemap_url_count': sitemap_urls,
        'kofi_status': 'configured'
    }
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    print(json.dumps(stats, indent=2))

if __name__ == '__main__':
    main()
