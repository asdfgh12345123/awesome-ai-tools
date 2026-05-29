#!/usr/bin/env python3
"""Generate products and affiliate disclosure pages."""
import os
from datetime import datetime, timezone

USERNAME = 'asdfgh12345123'
BASE_URL = f'https://{USERNAME}.github.io/awesome-ai-tools'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

NAV = '<nav><a href="' + BASE_URL + '/">Home</a> <a href="' + BASE_URL + '/tools/">Tools</a> <a href="' + BASE_URL + '/pricing/">Pricing</a> <a href="' + BASE_URL + '/products/">Products</a></nav>'
SUPPORT_CTA = '<div class="cta"><p>If this saved you time, consider supporting the project: <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or <a href="https://ifdian.net/a/aitoolshub">支持爱发电</a>.</p></div>'

def page_wrap(title, description, canonical, body):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><style>body{{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}}a{{color:#818cf8}}.wrap{{max-width:900px;margin:0 auto}}.cta{{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:16px;margin-top:24px}}.card{{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:20px;margin:16px 0}}.card h3{{margin-top:0;color:#818cf8}}.status{{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.8em;margin-left:8px}}.available{{background:#064e3b;color:#6ee7b7}}.coming{{background:#7c2d12;color:#fdba74}}h1{{color:#818cf8}}ul{{margin-left:18px}}nav{{margin-bottom:24px}}nav a{{margin-right:12px}}.disclaimer{{color:#94a3b8;font-size:0.85em;margin-top:16px}}</style></head><body><div class="wrap">{NAV}{body}{SUPPORT_CTA}</div></body></html>'''


# === PRODUCTS PAGE ===
print('Generating products page...')
products_body = f'''
<h1>Digital Products</h1>
<p>Useful resources for AI practitioners. These are self-serve digital products related to AI tools, automation, and safety.</p>
<p class="disclaimer"><small>Products listed here are for informational purposes. No fake reviews, sales counts, or income claims.</small></p>

<div class="card">
  <h3>AI Tools Pricing Sheet <span class="status coming">Coming soon</span></h3>
  <p>A structured spreadsheet tracking pricing, features, and free-tier limits for 50+ popular AI tools. Updated periodically.</p>
  <p>Format: Google Sheets / CSV</p>
  <p><a href="https://ko-fi.com/aitoolshub">Get notified on Ko-fi</a></p>
</div>

<div class="card">
  <h3>Codex Automation Starter Kit <span class="status coming">Coming soon</span></h3>
  <p>A ready-to-use template with GitHub Actions, Python scripts, and documentation for automating a static content site similar to this one.</p>
  <p>Format: GitHub repository template</p>
  <p><a href="https://ko-fi.com/aitoolshub">Get notified on Ko-fi</a></p>
</div>

<div class="card">
  <h3>AI Agent Safety Checklist <span class="status coming">Coming soon</span></h3>
  <p>A practical checklist for evaluating AI agent deployments, covering permissions, guardrails, logging, and rollback strategies.</p>
  <p>Format: PDF / Markdown</p>
  <p><a href="https://ko-fi.com/aitoolshub">Get notified on Ko-fi</a></p>
</div>

<p class="disclaimer"><small>These products are not yet available. Join the Ko-fi or Afdian page to be notified when they launch. Last updated: {NOW}.</small></p>
'''

products_html = page_wrap(
    'Digital Products - AI Tools Hub',
    'Self-serve digital products for AI practitioners: pricing sheets, automation kits, and safety checklists.',
    f'{BASE_URL}/products/',
    products_body
)
os.makedirs('products', exist_ok=True)
with open('products/index.html', 'w', encoding='utf-8') as f:
    f.write(products_html)
print('  Generated products/index.html')


# === AFFILIATE DISCLOSURE PAGE ===
print('Generating affiliate-disclosure page...')
disclosure_body = f'''
<h1>Affiliate Disclosure</h1>

<p>Some of the links on AI Tools Hub are affiliate links. This means that if you click on the link and make a purchase, we may receive a commission at no additional cost to you.</p>

<h2>What This Means</h2>
<ul>
  <li>We only recommend tools and products that we have reviewed or that are widely recognized in the AI community.</li>
  <li>Affiliate commissions help support the maintenance and growth of this project.</li>
  <li>You will never pay more by using an affiliate link.</li>
  <li>When an affiliate link is not available, we link directly to the official website.</li>
</ul>

<h2>Current Affiliate Status</h2>
<p>As of {NOW}, this project does not have active affiliate partnerships. All tool links point directly to official websites.</p>
<p>When affiliate links are added in the future, they will be clearly labeled on the relevant pages.</p>

<h2>Our Commitment</h2>
<ul>
  <li>We do not accept payment for positive reviews.</li>
  <li>We do not fabricate tool ratings, user reviews, or income claims.</li>
  <li>We do not use affiliate links for tools we would not recommend.</li>
  <li>Tool pricing is labeled as Free, Freemium, Paid, or Unknown based on publicly available information.</li>
</ul>

<h2>Contact</h2>
<p>If you have questions about our affiliate practices, please reach out via <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or open an issue on <a href="https://github.com/{USERNAME}/awesome-ai-tools">GitHub</a>.</p>
'''

disclosure_html = page_wrap(
    'Affiliate Disclosure - AI Tools Hub',
    'How AI Tools Hub uses affiliate links and our commitment to transparency.',
    f'{BASE_URL}/affiliate-disclosure/',
    disclosure_body
)
os.makedirs('affiliate-disclosure', exist_ok=True)
with open('affiliate-disclosure/index.html', 'w', encoding='utf-8') as f:
    f.write(disclosure_html)
print('  Generated affiliate-disclosure/index.html')

print('\nAll product and disclosure pages generated.')
