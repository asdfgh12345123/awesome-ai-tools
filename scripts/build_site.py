#!/usr/bin/env python3
import json, os

DATA_DIR = 'data'
OUTPUT_DIR = '.'

with open(os.path.join(DATA_DIR, 'tools.json'), 'r', encoding='utf-8-sig') as f:
    tools = json.load(f)
with open(os.path.join(DATA_DIR, 'categories.json'), 'r', encoding='utf-8-sig') as f:
    categories = json.load(f)
with open(os.path.join(DATA_DIR, 'prompts.json'), 'r', encoding='utf-8-sig') as f:
    prompts = json.load(f)

print('Building site from data files...')
os.makedirs(os.path.join(OUTPUT_DIR, 'tools'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, 'prompts'), exist_ok=True)

html = []
html.append('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">')
html.append('<title>AI Tools Directory - Generated Data Page</title>')
html.append('<meta name="description" content="Data-generated AI tools directory page with curated tools by category.">')
html.append('<link rel="canonical" href="https://asdfgh12345123.github.io/awesome-ai-tools/tools/generated.html">')
html.append('<style>body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}a{color:#818cf8}h1{color:#818cf8}h2{margin-top:24px}ul{margin-left:20px}li{margin:6px 0} .nav{margin-bottom:24px} .nav a{margin-right:12px}</style></head><body>')
html.append('<div class="nav"><a href="../">Home</a><a href="./">Tools</a><a href="../prompts/">Prompts</a></div>')
html.append('<h1>AI Tools Directory (Data Build)</h1>')
for cat_id, cat_info in categories.items():
    cat_tools = [t for t in tools if t.get('category') == cat_id]
    if not cat_tools:
        continue
    html.append(f'<h2>{cat_info["name"]}</h2><ul>')
    for t in cat_tools:
        html.append(f'<li><a href="{t["url"]}">{t["name"]} — {t.get("pricing","Unknown")}</a><br><span>{t.get("description","")}</span></li>')
    html.append('</ul>')
html.append('</body></html>')

tools_path = os.path.join(OUTPUT_DIR, 'tools', 'generated.html')
with open(tools_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
print(f'  Generated {tools_path}')

html2 = []
html2.append('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">')
html2.append('<title>ChatGPT Prompts - Generated Data Page</title>')
html2.append('<meta name="description" content="Data-generated prompt library for ChatGPT and other AI assistants.">')
html2.append('<link rel="canonical" href="https://asdfgh12345123.github.io/awesome-ai-tools/prompts/generated.html">')
html2.append('<style>body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}a{color:#818cf8}h1{color:#818cf8}h2{margin-top:24px}pre{background:#1e293b;border:1px solid #334155;border-radius:8px;padding:12px;white-space:pre-wrap} .nav{margin-bottom:24px} .nav a{margin-right:12px}</style></head><body>')
html2.append('<div class="nav"><a href="../">Home</a><a href="../tools/">Tools</a><a href="./">Prompts</a></div>')
html2.append('<h1>Prompt Library (Data Build)</h1>')
by_cat = {}
for p in prompts:
    by_cat.setdefault(p.get('category', 'general'), []).append(p)
for cat, items in by_cat.items():
    html2.append(f'<h2>{cat.title()}</h2>')
    for p in items:
        html2.append(f'<h3>{p.get("title","Untitled")}</h3><pre>{p.get("prompt","")}</pre>')
html2.append('</body></html>')

prompts_path = os.path.join(OUTPUT_DIR, 'prompts', 'generated.html')
with open(prompts_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html2))
print(f'  Generated {prompts_path}')
print('Build complete!')
