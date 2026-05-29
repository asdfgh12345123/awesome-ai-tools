#!/usr/bin/env python3
"""Generate products and affiliate disclosure pages (Chinese)."""
import os
from datetime import datetime, timezone

USERNAME = 'asdfgh12345123'
BASE_URL = f'https://{USERNAME}.github.io/awesome-ai-tools'
AFDIAN_URL = 'https://www.ifdian.net/item/61f89c485b6311f1b8bd5254001e7c00'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

NAV = '<nav><a href="' + BASE_URL + '/">Home</a> <a href="' + BASE_URL + '/tools/">Tools</a> <a href="' + BASE_URL + '/pricing/">Pricing</a> <a href="' + BASE_URL + '/products/">Products</a></nav>'
SUPPORT_CTA = '<div class="cta"><p>支持本项目：<a href="https://ko-fi.com/aitoolshub">Ko-fi</a> 或 <a href="https://ifdian.net/a/aitoolshub">爱发电</a></p></div>'


def page_wrap(title, description, canonical, body):
    return (
        '<!DOCTYPE html><html lang="zh-CN"><head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        '<title>' + title + '</title>'
        '<meta name="description" content="' + description + '">'
        '<link rel="canonical" href="' + canonical + '">'
        '<meta property="og:title" content="' + title + '">'
        '<meta property="og:description" content="' + description + '">'
        '<meta property="og:type" content="website">'
        '<meta property="og:locale" content="zh_CN">'
        '<style>'
        'body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;padding:24px;line-height:1.8}'
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
        'li{margin:6px 0}'
        'nav{margin-bottom:24px}'
        'nav a{margin-right:12px}'
        '.disclaimer{color:#94a3b8;font-size:0.85em;margin-top:16px}'
        '.notice{background:#1e3a5f;border:1px solid #3b5998;border-radius:8px;padding:12px;margin:12px 0;color:#93c5fd}'
        '</style>'
        '</head><body><div class="wrap">' + NAV + body + SUPPORT_CTA + '</div></body></html>'
    )


print('Generating products page...')
products_body = (
    '<h1>数字产品与资源包</h1>'
    '<p>面向 AI 工具、Codex 自动化和项目整理的轻量资源包。</p>'
    '<p class="disclaimer"><small>本页面仅作产品展示，不承诺收益、不提供账号、token 或自动赚钱脚本。</small></p>'
    '<div class="card featured">'
    '  <h3>Codex 自动化入门工具包 <span class="status free">Lite 免费预览</span> <span class="status available">Pro v1.3 中文版</span></h3>'
    '  <p>一套实用的工具包，帮助你用 Codex 和 GitHub Actions 把本地项目整理成可自动维护的工作流。</p>'
    '  <p><strong>Lite 免费预览</strong>：在 GitHub 上查看基本结构、清单和提示词，适合了解思路。</p>'
    '  <p><strong>Pro v1.3 中文版（49 元）</strong>：完整包，包含 61 条 Codex 提示词模板、42 个常见错误排查、8 个 GitHub Actions workflow 模板、8 个实战案例、安全检查清单、质量检查报告等。</p>'
    '  <p><a class="btn primary" href="' + AFDIAN_URL + '">在爱发电购买 Pro v1.3 中文版</a> <a class="btn secondary" href="codex-automation-starter-kit/">查看产品详情</a></p>'
    '  <div class="notice">爱发电商品详情在未登录状态下可能显示不完整，如页面内容为空，请登录后查看。购买前也可以先阅读本站介绍和 Lite 免费预览。</div>'
    '  <p class="disclaimer"><small>Ko-fi：暂未上架。</small></p>'
    '</div>'
    '<div class="card">'
    '  <h3>AI Tools Pricing Sheet <span class="status coming">即将上线</span></h3>'
    '  <p>结构化的表格，跟踪 50+ 常用 AI 工具的价格、功能和免费额度。</p>'
    '  <p>格式：Google Sheets / CSV</p>'
    '  <p><a href="https://ko-fi.com/aitoolshub">在 Ko-fi 获取通知</a></p>'
    '</div>'
    '<div class="card">'
    '  <h3>AI Agent Safety Checklist <span class="status coming">即将上线</span></h3>'
    '  <p>实用清单，用于评估 AI Agent 部署的权限、护栏、日志和回滚策略。</p>'
    '  <p>格式：PDF / Markdown</p>'
    '  <p><a href="https://ko-fi.com/aitoolshub">在 Ko-fi 获取通知</a></p>'
    '</div>'
    '<p class="disclaimer"><small>关注 Ko-fi 或爱发电获取新产品通知。最后更新：' + NOW + '。</small></p>'
)

products_html = page_wrap(
    '数字产品 - AI Tools Hub',
    '面向 AI 工具、Codex 自动化和项目整理的轻量资源包。',
    BASE_URL + '/products/',
    products_body
)
os.makedirs('products', exist_ok=True)
with open('products/index.html', 'w', encoding='utf-8') as f:
    f.write(products_html)
print('  Generated products/index.html')


print('Generating affiliate-disclosure page...')
disclosure_body = (
    '<h1>联盟链接声明</h1>'
    '<p>AI Tools Hub 部分链接为联盟链接。如果你通过这些链接购买产品，我们可能会获得佣金，但不会增加你的费用。</p>'
    '<h2>当前状态</h2>'
    '<p>目前本项目没有活跃的联盟合作。所有工具链接直接指向官方网站。</p>'
    '<h2>我们的承诺</h2>'
    '<ul>'
    '<li>不接受有偿推荐</li>'
    '<li>不编造工具评分、用户评价或收入数据</li>'
    '<li>不使用联盟链接推荐不会使用的工具</li>'
    '<li>工具价格标签基于公开信息：Free、Freemium、Paid 或 Unknown</li>'
    '</ul>'
    '<h2>联系</h2>'
    '<p>如有疑问，请通过 <a href="https://ko-fi.com/aitoolshub">Ko-fi</a> 或在 <a href="https://github.com/' + USERNAME + '/awesome-ai-tools">GitHub</a> 提交 Issue。</p>'
)

disclosure_html = page_wrap(
    '联盟链接声明 - AI Tools Hub',
    'AI Tools Hub 的联盟链接使用方式和透明度承诺。',
    BASE_URL + '/affiliate-disclosure/',
    disclosure_body
)
os.makedirs('affiliate-disclosure', exist_ok=True)
with open('affiliate-disclosure/index.html', 'w', encoding='utf-8') as f:
    f.write(disclosure_html)
print('  Generated affiliate-disclosure/index.html')
print('All product and disclosure pages generated.')
