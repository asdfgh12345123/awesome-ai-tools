#!/usr/bin/env python3
"""Generate pricing, alternatives, compare, tool detail, and new guide pages."""
import json, os
from datetime import datetime, timezone

DATA_DIR = 'data'
GUIDES_DIR = 'guides'
USERNAME = 'asdfgh12345123'
BASE_URL = f'https://{USERNAME}.github.io/awesome-ai-tools'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8-sig') as f:
        return json.load(f)

tools = load_json('tools.json')
pricing = load_json('pricing.json')
affiliates = load_json('affiliates.json')
categories = load_json('categories.json')

# Build lookup maps
pricing_map = {p['slug']: p for p in pricing}
aff_map = {a['slug']: a for a in affiliates}

def get_link(t):
    slug = t['name'].lower().replace(' ', '-')
    aff = aff_map.get(slug, {})
    if aff.get('affiliate_url') and aff.get('affiliate_status') == 'active':
        return aff['affiliate_url']
    return t['url']

def get_alt_text(t):
    return t['url']

SUPPORT_CTA = '<div class="cta"><p>If this saved you time, consider supporting the project: <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or <a href="https://ifdian.net/a/aitoolshub">支持爱发电</a>.</p></div>'
DISCLAIMER = '<p class="disclaimer"><small>Prices and availability may change. Last verified: ' + NOW + '. Always check the official website for current pricing.</small></p>'
AFF_DISCLOSURE = '<p class="disclaimer"><small><a href="' + BASE_URL + '/affiliate-disclosure/">Affiliate Disclosure</a>: Some links may be affiliate links. We may earn a commission at no extra cost to you.</small></p>'
NAV = '<nav><a href="' + BASE_URL + '/">Home</a> <a href="' + BASE_URL + '/tools/">Tools</a> <a href="' + BASE_URL + '/pricing/">Pricing</a> <a href="' + BASE_URL + '/alternatives/">Alternatives</a> <a href="' + BASE_URL + '/compare/">Compare</a> <a href="' + BASE_URL + '/products/">Products</a></nav>'

def page_wrap(title, description, canonical, body, extra_head=''):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:type" content="website">{extra_head}<style>body{{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}}a{{color:#818cf8}}table{{width:100%;border-collapse:collapse;margin:16px 0}}th,td{{padding:8px;border-bottom:1px solid #334155;text-align:left}}.wrap{{max-width:960px;margin:0 auto}}.cta{{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:16px;margin-top:24px}}.disclaimer{{color:#94a3b8;font-size:0.85em;margin-top:16px}}h1{{color:#818cf8}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:16px 0}}.card{{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:16px}}.card h3{{margin-top:0}}.badge{{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.8em}}.free{{background:#064e3b;color:#6ee7b7}}.paid{{background:#7c2d12;color:#fdba74}}.freemium{{background:#1e3a5f;color:#93c5fd}}.unknown{{background:#374151;color:#d1d5db}}ul{{margin-left:18px}}nav{{margin-bottom:24px}}nav a{{margin-right:12px}}</style></head><body><div class="wrap">{NAV}{body}{SUPPORT_CTA}</div></body></html>'''


def pricing_badge(t):
    slug = t['name'].lower().replace(' ', '-')
    p = pricing_map.get(slug, {})
    model = p.get('pricing_model', t.get('pricing', 'Unknown')).lower()
    if 'free' in model and ('pro' in model or '/' in model):
        return '<span class="badge freemium">Freemium</span>'
    elif 'free' in model:
        return '<span class="badge free">Free</span>'
    elif 'paid' in model:
        return '<span class="badge paid">Paid</span>'
    return '<span class="badge unknown">Unknown</span>'


# === 1. PRICING PAGE ===
print('Generating pricing page...')
cards = []
for t in tools:
    slug = t['name'].lower().replace(' ', '-')
    p = pricing_map.get(slug, {})
    link = get_link(t)
    cards.append(f'<div class="card"><h3><a href="{link}">{t["name"]}</a> {pricing_badge(t)}</h3><p>{t.get("description","")}</p><p>Category: {t.get("category","")} | Model: {p.get("pricing_model", t.get("pricing","Unknown"))}</p><p><a href="../tools/{slug}.html">Details &amp; alternatives</a></p></div>')

pricing_html = page_wrap(
    'AI Tools Pricing Watch - AI Tools Hub',
    'Compare pricing for popular AI tools. Labels show Free, Freemium, Paid, or Unknown based on public information.',
    f'{BASE_URL}/pricing/',
    f'<h1>AI Tools Pricing Watch</h1><p>Track pricing labels for popular AI tools. We use Free, Freemium, Paid, or Unknown when exact pricing cannot be confirmed. {DISCLAIMER}</p><div class="grid">{"".join(cards)}</div>{AFF_DISCLOSURE}'
)
os.makedirs('pricing', exist_ok=True)
with open('pricing/index.html', 'w', encoding='utf-8') as f:
    f.write(pricing_html)
print('  Generated pricing/index.html')


# === 2. ALTERNATIVES PAGE ===
print('Generating alternatives page...')
alt_sections = []
# Group by category
by_cat = {}
for t in tools:
    by_cat.setdefault(t.get('category', 'other'), []).append(t)

for cat_id, cat_tools in by_cat.items():
    cat_name = categories.get(cat_id, {}).get('name', cat_id.title())
    items = []
    for t in cat_tools:
        slug = t['name'].lower().replace(' ', '-')
        alts = [o for o in cat_tools if o['name'] != t['name']][:3]
        if alts:
            alt_links = ', '.join(f'<a href="../tools/{a["name"].lower().replace(" ","-")}.html">{a["name"]}</a>' for a in alts)
            items.append(f'<li><strong><a href="../tools/{slug}.html">{t["name"]}</a></strong> - {t.get("description","")} <br>Alternatives: {alt_links}</li>')
    if items:
        alt_sections.append(f'<h2>{cat_name}</h2><ul>{"".join(items)}</ul>')

alt_html = page_wrap(
    'AI Tools Alternatives - AI Tools Hub',
    'Find alternatives to popular AI tools by category. Compare options for coding, writing, research, and image generation.',
    f'{BASE_URL}/alternatives/',
    f'<h1>AI Tools Alternatives</h1><p>Looking for a different option? Browse alternatives grouped by category. {DISCLAIMER}</p>{"".join(alt_sections)}{AFF_DISCLOSURE}'
)
os.makedirs('alternatives', exist_ok=True)
with open('alternatives/index.html', 'w', encoding='utf-8') as f:
    f.write(alt_html)
print('  Generated alternatives/index.html')


# === 3. COMPARE PAGE ===
print('Generating compare page...')
rows = []
for t in tools:
    slug = t['name'].lower().replace(' ', '-')
    p = pricing_map.get(slug, {})
    rows.append(f'<tr><td><a href="{get_link(t)}">{t["name"]}</a></td><td>{t.get("category","")}</td><td>{p.get("pricing_model", t.get("pricing","Unknown"))}</td><td>{"Yes" if t.get("open_source") else "No"}</td><td>{t.get("description","")}</td></tr>')

compare_html = page_wrap(
    'Compare AI Tools - AI Tools Hub',
    'Side-by-side comparison of AI tools by category, pricing model, and open-source status.',
    f'{BASE_URL}/compare/',
    f'<h1>Compare AI Tools</h1><p>Compare popular AI tools at a glance. {DISCLAIMER}</p><table><tr><th>Tool</th><th>Category</th><th>Pricing</th><th>Open Source</th><th>Description</th></tr>{"".join(rows)}</table>{AFF_DISCLOSURE}'
)
os.makedirs('compare', exist_ok=True)
with open('compare/index.html', 'w', encoding='utf-8') as f:
    f.write(compare_html)
print('  Generated compare/index.html')


# === 4. TOOL DETAIL PAGES ===
print('Generating tool detail pages...')
os.makedirs('tools', exist_ok=True)
for t in tools:
    slug = t['name'].lower().replace(' ', '-')
    p = pricing_map.get(slug, {})
    link = get_link(t)
    # Find alternatives in same category
    cat_tools = by_cat.get(t.get('category', ''), [])
    alts = [o for o in cat_tools if o['name'] != t['name']][:5]
    alt_list = ''.join(f'<li><a href="{o["name"].lower().replace(" ","-")}.html">{o["name"]}</a> - {o.get("description","")}</li>' for o in alts) if alts else '<li>No alternatives listed yet.</li>'

    tool_html = page_wrap(
        f'{t["name"]} - AI Tools Hub',
        f'{t.get("description","AI tool")} - pricing, alternatives, and details.',
        f'{BASE_URL}/tools/{slug}.html',
        f'<h1>{t["name"]}</h1><p>{t.get("description","")}</p><p><a href="{link}">Visit {t["name"]}</a> {pricing_badge(t)}</p><table><tr><th>Category</th><th>Pricing Model</th><th>Open Source</th></tr><tr><td>{t.get("category","")}</td><td>{p.get("pricing_model", t.get("pricing","Unknown"))}</td><td>{"Yes" if t.get("open_source") else "No"}</td></tr></table><h2>Alternatives</h2><ul>{alt_list}</ul>{DISCLAIMER}{AFF_DISCLOSURE}',
        f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{t["name"]}","applicationCategory":"DeveloperTool","operatingSystem":"Web","url":"{t["url"]}"}}</script>'
    )
    with open(f'tools/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(tool_html)
print(f'  Generated {len(tools)} tool detail pages')


# === 5. NEW GUIDE: Cheapest AI Coding Tools ===
print('Generating guide: cheapest-ai-coding-tools...')
coding_tools = [t for t in tools if t.get('category') == 'coding']
rows = ''.join(f'<tr><td><a href="{get_link(t)}">{t["name"]}</a></td><td>{pricing_map.get(t["name"].lower().replace(" ","-"), {}).get("pricing_model", t.get("pricing","Unknown"))}</td><td>{"Yes" if t.get("open_source") else "No"}</td><td>{t.get("description","")}</td></tr>' for t in coding_tools)
guide1 = page_wrap(
    'Cheapest AI Coding Tools in 2026 - AI Tools Hub',
    'Compare the most affordable AI coding tools, including free and open-source options.',
    f'{BASE_URL}/guides/cheapest-ai-coding-tools.html',
    f'<h1>Cheapest AI Coding Tools in 2026</h1><p>Looking for affordable AI coding assistance? These tools offer free plans or low-cost subscriptions. {DISCLAIMER}</p><table><tr><th>Tool</th><th>Pricing</th><th>Open Source</th><th>Description</th></tr>{rows}</table><p>See also: <a href="../pricing/">Full pricing watch</a> | <a href="../alternatives/">Alternatives</a></p>{AFF_DISCLOSURE}',
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is the cheapest AI coding tool?","acceptedAnswer":{"@type":"Answer","text":"Free and open-source options like Aider, Continue, and Ollama offer coding assistance at no cost. Freemium tools like Cursor offer free tiers with paid upgrades."}},{"@type":"Question","name":"Are free AI coding tools good enough?","acceptedAnswer":{"@type":"Answer","text":"Many free AI coding tools provide useful code completion and chat features. Open-source tools run locally and do not require paid subscriptions."}}]}</script>'
)
with open(os.path.join(GUIDES_DIR, 'cheapest-ai-coding-tools.html'), 'w', encoding='utf-8') as f:
    f.write(guide1)
print('  Generated guides/cheapest-ai-coding-tools.html')


# === 6. NEW GUIDE: Free AI Tools with Generous Limits ===
print('Generating guide: free-ai-tools-with-generous-limits...')
free_tools = [t for t in tools if 'free' in str(t.get('pricing', '')).lower()]
rows = ''.join(f'<tr><td><a href="{get_link(t)}">{t["name"]}</a></td><td>{t.get("pricing","Unknown")}</td><td>{t.get("category","")}</td><td>{t.get("description","")}</td></tr>' for t in free_tools)
guide2 = page_wrap(
    'Free AI Tools with Generous Limits in 2026 - AI Tools Hub',
    'AI tools that offer meaningful free tiers without requiring a credit card.',
    f'{BASE_URL}/guides/free-ai-tools-with-generous-limits.html',
    f'<h1>Free AI Tools with Generous Limits in 2026</h1><p>These tools offer free access or generous free tiers. Always check the official website for current limits. {DISCLAIMER}</p><table><tr><th>Tool</th><th>Pricing</th><th>Category</th><th>Description</th></tr>{rows}</table><p>See also: <a href="../pricing/">Full pricing watch</a> | <a href="../compare/">Compare tools</a></p>{AFF_DISCLOSURE}',
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Which AI tools have the best free plans?","acceptedAnswer":{"@type":"Answer","text":"Claude, ChatGPT, Perplexity, and Ollama all offer free access with varying feature limits. Open-source tools like Stable Diffusion and Aider are fully free."}},{"@type":"Question","name":"Do free AI tools require a credit card?","acceptedAnswer":{"@type":"Answer","text":"Many free AI tools do not require a credit card. Always check the official pricing page for current requirements."}}]}</script>'
)
with open(os.path.join(GUIDES_DIR, 'free-ai-tools-with-generous-limits.html'), 'w', encoding='utf-8') as f:
    f.write(guide2)
print('  Generated guides/free-ai-tools-with-generous-limits.html')


# === 7. NEW GUIDE: Codex vs Claude Code vs Gemini CLI ===
print('Generating guide: codex-vs-claude-code-vs-gemini-cli...')
comparison_items = [
    ('OpenAI Codex', 'https://openai.com/index/codex/', 'CLI-based AI coding agent from OpenAI. Runs in terminal and can execute commands.', 'Paid', 'No'),
    ('Claude Code', 'https://www.anthropic.com/claude-code', 'CLI-based AI coding agent from Anthropic. Focuses on agentic coding workflows.', 'Paid', 'No'),
    ('Gemini CLI', 'https://github.com/google-gemini/gemini-cli', 'Google Gemini CLI tool for terminal-based AI coding assistance.', 'Free', 'Yes'),
]
rows = ''.join(f'<tr><td><a href="{url}">{name}</a></td><td>{pricing}</td><td>{oss}</td><td>{desc}</td></tr>' for name, url, desc, pricing, oss in comparison_items)
guide3 = page_wrap(
    'Codex vs Claude Code vs Gemini CLI Comparison - AI Tools Hub',
    'Compare OpenAI Codex, Claude Code, and Gemini CLI for terminal-based AI coding workflows.',
    f'{BASE_URL}/guides/codex-vs-claude-code-vs-gemini-cli.html',
    f'<h1>Codex vs Claude Code vs Gemini CLI</h1><p>Three terminal-based AI coding tools compared. Pricing and availability may change; always check the official website. {DISCLAIMER}</p><table><tr><th>Tool</th><th>Pricing</th><th>Open Source</th><th>Description</th></tr>{rows}</table><h2>When to Use Each</h2><ul><li><strong>Codex</strong>: Best for OpenAI ecosystem users who want a CLI agent with cloud execution.</li><li><strong>Claude Code</strong>: Best for Anthropic users who want agentic terminal workflows with Claude models.</li><li><strong>Gemini CLI</strong>: Best for free/open-source users who want Google Gemini capabilities in terminal.</li></ul><p>See also: <a href="../guides/best-ai-tools-for-coding.html">Best AI Tools for Coding</a> | <a href="../compare/">Compare all tools</a></p>{AFF_DISCLOSURE}',
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is Gemini CLI free?","acceptedAnswer":{"@type":"Answer","text":"Yes, Gemini CLI is open-source and free to use. Codex and Claude Code require paid API access or subscriptions."}},{"@type":"Question","name":"Which CLI coding tool is best?","acceptedAnswer":{"@type":"Answer","text":"It depends on your needs. Codex is best for OpenAI users, Claude Code for Anthropic users, and Gemini CLI for free/open-source workflows."}}]}</script>'
)
with open(os.path.join(GUIDES_DIR, 'codex-vs-claude-code-vs-gemini-cli.html'), 'w', encoding='utf-8') as f:
    f.write(guide3)
print('  Generated guides/codex-vs-claude-code-vs-gemini-cli.html')

print('\nAll pricing and alternatives pages generated successfully.')
