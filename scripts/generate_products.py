#!/usr/bin/env python3
"""Generate products and affiliate disclosure pages."""
import os
from datetime import datetime, timezone

USERNAME = 'asdfgh12345123'
BASE_URL = f'https://{USERNAME}.github.io/awesome-ai-tools'
AFDIAN_URL = 'https://www.ifdian.net/item/61f89c485b6311f1b8bd5254001e7c00'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

NAV = '<nav><a href="' + BASE_URL + '/">Home</a> <a href="' + BASE_URL + '/tools/">Tools</a> <a href="' + BASE_URL + '/pricing/">Pricing</a> <a href="' + BASE_URL + '/products/">Products</a></nav>'
SUPPORT_CTA = '<div class="cta"><p>Support the project: <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or <a href="https://ifdian.net/a/aitoolshub">Afdian</a></p></div>'


def page_wrap(title, description, canonical, body):
    return (
        '<!DOCTYPE html><html lang="en"><head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        '<title>' + title + '</title>'
        '<meta name="description" content="' + description + '">'
        '<link rel="canonical" href="' + canonical + '">'
        '<meta property="og:title" content="' + title + '">'
        '<meta property="og:description" content="' + description + '">'
        '<meta property="og:type" content="website">'
        '<style>'
        'body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px}'
        'a{color:#818cf8}'
        '.wrap{max-width:900px;margin:0 auto}'
        '.cta{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:16px;margin-top:24px}'
        '.btn{display:inline-block;padding:12px 20px;border-radius:8px;font-weight:600;text-decoration:none;margin:8px 4px}'
        '.btn.primary{background:#818cf8;color:#0f172a}'
        '.btn.secondary{background:#1e293b;color:#e2e8f0;border:1px solid #334155}'
        '.card{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:20px;margin:16px 0}'
        '.card h3{margin-top:0;color:#818cf8}'
        '.card.featured{border-color:#818cf8;box-shadow:0 0 12px rgba(129,140,248,0.2)}'
        '.status{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.8em;margin-left:8px}'
        '.free{background:#064e3b;color:#6ee7b7}'
        '.available{background:#064e3b;color:#6ee7b7}'
        '.coming{background:#374151;color:#d1d5db}'
        'h1{color:#818cf8}'
        'h2{margin-top:24px;color:#818cf8}'
        'ul{margin-left:18px}'
        'nav{margin-bottom:24px}'
        'nav a{margin-right:12px}'
        '.disclaimer{color:#94a3b8;font-size:0.85em;margin-top:16px}'
        '.notice{background:#1e3a5f;border:1px solid #3b5998;border-radius:8px;padding:12px;margin:12px 0;color:#93c5fd}'
        '</style>'
        '</head><body><div class="wrap">' + NAV + body + SUPPORT_CTA + '</div></body></html>'
    )


print('Generating products page...')
products_body = (
    '<h1>Digital Products</h1>'
    '<p>Useful resources for AI practitioners. These are self-serve digital products related to AI tools, automation, and safety.</p>'
    '<p class="disclaimer"><small>Products listed here are for informational purposes. No fake reviews, sales counts, or income claims.</small></p>'
    '<div class="card featured">'
    '  <h3>Codex Automation Starter Kit <span class="status free">Lite: Free</span> <span class="status available">Pro v1.3: Available on Afdian</span></h3>'
    '  <p>A practical, self-contained starter kit for organizing local projects into maintainable, automated workflows using OpenAI Codex and GitHub Actions.</p>'
    '  <p><strong>Lite version (free)</strong>: Preview the structure, checklists, and prompts on GitHub. Good for understanding the approach.</p>'
    '  <p><strong>Pro version v1.3 (49 CNY)</strong>: Chinese language package with 61 Codex prompt templates, 42 common error fixes, 8 workflow YAML templates, 8 real-world examples, quality control checklist, source attribution, and more.</p>'
    '  <p><a class="btn primary" href="' + AFDIAN_URL + '">在爱发电购买 Pro v1.3 中文版</a> <a class="btn secondary" href="codex-automation-starter-kit/">View product details</a></p>'
    '  <div class="notice">爱发电商品详情在未登录状态下可能显示不完整，如页面内容为空，请登录后查看。购买前也可以先阅读本站介绍和 Lite 免费预览。</div>'
    '  <p class="disclaimer"><small>Ko-fi: Not listed yet.</small></p>'
    '</div>'
    '<div class="card">'
    '  <h3>AI Tools Pricing Sheet <span class="status coming">Coming soon</span></h3>'
    '  <p>A structured spreadsheet tracking pricing, features, and free-tier limits for 50+ popular AI tools. Updated periodically.</p>'
    '  <p>Format: Google Sheets / CSV</p>'
    '  <p><a href="https://ko-fi.com/aitoolshub">Get notified on Ko-fi</a></p>'
    '</div>'
    '<div class="card">'
    '  <h3>AI Agent Safety Checklist <span class="status coming">Coming soon</span></h3>'
    '  <p>A practical checklist for evaluating AI agent deployments, covering permissions, guardrails, logging, and rollback strategies.</p>'
    '  <p>Format: PDF / Markdown</p>'
    '  <p><a href="https://ko-fi.com/aitoolshub">Get notified on Ko-fi</a></p>'
    '</div>'
    '<p class="disclaimer"><small>Join the Ko-fi or Afdian page to be notified when new products launch. Last updated: ' + NOW + '.</small></p>'
)

products_html = page_wrap(
    'Digital Products - AI Tools Hub',
    'Self-serve digital products for AI practitioners: pricing sheets, automation kits, and safety checklists.',
    BASE_URL + '/products/',
    products_body
)
os.makedirs('products', exist_ok=True)
with open('products/index.html', 'w', encoding='utf-8') as f:
    f.write(products_html)
print('  Generated products/index.html')


print('Generating affiliate-disclosure page...')
disclosure_body = (
    '<h1>Affiliate Disclosure</h1>'
    '<p>Some of the links on AI Tools Hub are affiliate links. This means that if you click on the link and make a purchase, we may receive a commission at no additional cost to you.</p>'
    '<h2>What This Means</h2>'
    '<ul>'
    '<li>We only recommend tools and products that we have reviewed or that are widely recognized in the AI community.</li>'
    '<li>Affiliate commissions help support the maintenance and growth of this project.</li>'
    '<li>You will never pay more by using an affiliate link.</li>'
    '<li>When an affiliate link is not available, we link directly to the official website.</li>'
    '</ul>'
    '<h2>Current Affiliate Status</h2>'
    '<p>This project does not have active affiliate partnerships. All tool links point directly to official websites.</p>'
    '<h2>Our Commitment</h2>'
    '<ul>'
    '<li>We do not accept payment for positive reviews.</li>'
    '<li>We do not fabricate tool ratings, user reviews, or income claims.</li>'
    '<li>We do not use affiliate links for tools we would not recommend.</li>'
    '<li>Tool pricing is labeled as Free, Freemium, Paid, or Unknown based on publicly available information.</li>'
    '</ul>'
    '<h2>Contact</h2>'
    '<p>If you have questions about our affiliate practices, please reach out via <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> or open an issue on <a href="https://github.com/' + USERNAME + '/awesome-ai-tools">GitHub</a>.</p>'
)

disclosure_html = page_wrap(
    'Affiliate Disclosure - AI Tools Hub',
    'How AI Tools Hub uses affiliate links and our commitment to transparency.',
    BASE_URL + '/affiliate-disclosure/',
    disclosure_body
)
os.makedirs('affiliate-disclosure', exist_ok=True)
with open('affiliate-disclosure/index.html', 'w', encoding='utf-8') as f:
    f.write(disclosure_html)
print('  Generated affiliate-disclosure/index.html')
print('All product and disclosure pages generated.')
