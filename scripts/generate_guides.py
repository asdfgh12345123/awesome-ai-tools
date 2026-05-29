#!/usr/bin/env python3
import json, os
from datetime import datetime

DATA_DIR = 'data'
GUIDES_DIR = 'guides'
USERNAME = 'asdfgh12345123'
BASE_URL = f'https://{USERNAME}.github.io/awesome-ai-tools'

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8-sig') as f:
        return json.load(f)

tools = load_json('tools.json')
categories = load_json('categories.json')
prompts = load_json('prompts.json')
models = load_json('models.json')
agents = load_json('agents.json')
rag = load_json('rag-tools.json')

os.makedirs(GUIDES_DIR, exist_ok=True)

def render(title, description, keywords, slug, h1, intro, body):
    nav = '<nav><a href="../">Home</a> <a href="../tools/">Tools</a> <a href="../prompts/">Prompts</a> <a href="../compare/">Compare</a></nav>'
    faq = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is this list regularly updated?","acceptedAnswer":{"@type":"Answer","text":"Yes. We review entries periodically and update pricing labels using Free, Freemium, Paid, or Unknown when exact pricing cannot be confirmed."}},{"@type":"Question","name":"Is this project free to use?","acceptedAnswer":{"@type":"Answer","text":"Yes. The directory, guides, and prompt resources are free to use, and optional support is available through Ko-fi and Afdian."}}]}</script>'
    cta = '<div class="cta"><p>If this saved you time, consider supporting the project: <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or <a href="https://ifdian.net/a/aitoolshub">爱发电</a>.</p></div>'
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><meta name="description" content="{description}"><meta name="keywords" content="{keywords}"><link rel="canonical" href="{BASE_URL}/guides/{slug}.html"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:type" content="article">{faq}<style>body{{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}}a{{color:#818cf8}}table{{width:100%;border-collapse:collapse}}th,td{{padding:8px;border-bottom:1px solid #334155;text-align:left}}.wrap{{max-width:900px;margin:0 auto}}.cta{{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:16px;margin-top:24px}}ul{{margin-left:18px}}h1{{color:#818cf8}}</style></head><body><div class="wrap">{nav}<h1>{h1}</h1><p>{intro}</p>{body}{cta}</div></body></html>'''

guide_pages = []

# 1 coding
cat_tools = [t for t in tools if t.get('category') == 'coding']
rows = ''.join(f'<tr><td>{t["name"]}</td><td>{t.get("pricing","Unknown")}</td><td>{t.get("description","")}</td></tr>' for t in cat_tools)
guide_pages.append(('best-ai-tools-for-coding', 'Best AI Tools for Coding in 2026', 'Find the best AI coding tools with practical use cases and current pricing labels.', 'AI tools for coding, best AI coding tools, AI code editor, coding assistants', 'Best AI Tools for Coding in 2026', 'This guide focuses on AI tools that help with software development, debugging, refactoring, and terminal workflows.', f'<h2>Comparison</h2><table><tr><th>Tool</th><th>Pricing</th><th>Description</th></tr>{rows}</table><h2>Also Useful</h2><ul><li><a href="../tools/">Browse full tools directory</a></li><li><a href="../compare/">Compare major AI models</a></li></ul>'))

# 2 writing
cat_tools = [t for t in tools if t.get('category') == 'writing']
rows = ''.join(f'<tr><td>{t["name"]}</td><td>{t.get("pricing","Unknown")}</td><td>{t.get("description","")}</td></tr>' for t in cat_tools)
guide_pages.append(('best-ai-tools-for-writing', 'Best AI Tools for Writing in 2026', 'AI writing assistants for long-form content, editing, marketing copy, and productivity.', 'AI tools for writing, AI writing assistant, writing tools, ChatGPT alternatives for writing', 'Best AI Tools for Writing in 2026', 'Use these tools to draft, edit, summarize, and repurpose written content faster.', f'<h2>Comparison</h2><table><tr><th>Tool</th><th>Pricing</th><th>Description</th></tr>{rows}</table><h2>Prompt Ideas</h2><ul><li><a href="../prompts/">Browse the prompt library</a></li><li><a href="../prompt-generator/">Use the prompt generator</a></li></ul>'))

# 3 free tools
free_tools = [t for t in tools if 'free' in str(t.get('pricing','')).lower()]
rows = ''.join(f'<tr><td>{t["name"]}</td><td>{t.get("pricing","Unknown")}</td><td>{t.get("description","")}</td></tr>' for t in free_tools)
guide_pages.append(('free-ai-tools', 'Best Free AI Tools in 2026', 'A focused list of free or freemium AI tools for coding, writing, research, and productivity.', 'free AI tools, best free AI, free AI apps, AI tools no cost', 'Best Free AI Tools in 2026', 'This guide highlights tools that can be used without a paid plan, or that offer meaningful free tiers.', f'<h2>Free and Freemium Picks</h2><table><tr><th>Tool</th><th>Pricing</th><th>Description</th></tr>{rows}</table>'))

# 4 prompts for coding
coding_prompts = [p for p in prompts if p.get('category') == 'coding']
items = ''.join(f'<h3>{p.get("title","Prompt")}</h3><pre>{p.get("prompt","")}</pre>' for p in coding_prompts)
guide_pages.append(('chatgpt-prompts-for-coding', 'ChatGPT Prompts for Coding in 2026', 'Copy-paste prompts for code review, debugging, testing, refactoring, and documentation.', 'ChatGPT prompts for coding, coding prompts, AI prompts for developers', 'ChatGPT Prompts for Coding in 2026', 'Use these prompts when you need faster debugging, cleaner refactors, and better explanations.', f'{items}<p>Browse more: <a href="../prompts/">full prompt library</a></p>'))

# 5 prompts for writing
writing_prompts = [p for p in prompts if p.get('category') == 'writing']
items = ''.join(f'<h3>{p.get("title","Prompt")}</h3><pre>{p.get("prompt","")}</pre>' for p in writing_prompts)
guide_pages.append(('chatgpt-prompts-for-writing', 'ChatGPT Prompts for Writing in 2026', 'Useful prompts for articles, emails, summaries, and content planning.', 'ChatGPT prompts for writing, writing prompts, content prompts', 'ChatGPT Prompts for Writing in 2026', 'Use these prompts for faster drafting and editing workflows.', f'{items}<p>Browse more: <a href="../prompts/">full prompt library</a></p>'))

# 6 agents comparison
rows = ''.join(f'<tr><td><a href="{a.get("url","#")}">{a["name"]}</a></td><td>{a.get("category","")}</td><td>{a.get("description","")}</td></tr>' for a in agents)
guide_pages.append(('ai-agents-framework-comparison', 'AI Agents Framework Comparison in 2026', 'Compare popular AI agent frameworks and resources in one place.', 'AI agents framework comparison, open source AI agents, AI agent tools', 'AI Agents Framework Comparison in 2026', 'This comparison is useful if you are evaluating agent frameworks and orchestration tools.', f'<h2>Frameworks</h2><table><tr><th>Name</th><th>Category</th><th>Description</th></tr>{rows}</table><p>Related repository: <a href="https://github.com/{USERNAME}/awesome-ai-agents">Awesome AI Agents</a></p>'))

# 7 rag comparison
rows = ''.join(f'<tr><td><a href="{r.get("url","#")}">{r["name"]}</a></td><td>{r.get("category","")}</td><td>{r.get("description","")}</td></tr>' for r in rag)
guide_pages.append(('rag-tools-comparison', 'RAG Tools Comparison in 2026', 'Compare RAG frameworks and related retrieval tooling for production use.', 'RAG tools comparison, RAG framework comparison, retrieval augmented generation tools', 'RAG Tools Comparison in 2026', 'Use this comparison when evaluating frameworks for retrieval-augmented generation workflows.', f'<h2>Tools</h2><table><tr><th>Name</th><th>Category</th><th>Description</th></tr>{rows}</table><p>Related repository: <a href="https://github.com/{USERNAME}/awesome-rag">Awesome RAG</a></p>'))

for slug, title, description, keywords, h1, intro, body in guide_pages:
    html = render(title, description, keywords, slug, h1, intro, body)
    path = os.path.join(GUIDES_DIR, f'{slug}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Generated {path}')

print(f'\nGenerated {len(guide_pages)} guide pages')
