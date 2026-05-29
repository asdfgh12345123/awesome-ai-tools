# PROJECT_STATUS.md

## 1. 项目目标

AI Tools Hub 的目标是维护一套公开、免费、可持续更新的 AI 资源矩阵，覆盖：

- AI 工具目录
- ChatGPT 提示词资源
- AI Agents 资源
- RAG 资源
- AI 模型对比
- 项目健康度与赞助入口

本项目不承诺收入、流量或排名结果。

## 2. 项目矩阵

### 主站仓库
- awesome-ai-tools: https://github.com/asdfgh12345123/awesome-ai-tools

### 专项仓库
- awesome-ai-agents: https://github.com/asdfgh12345123/awesome-ai-agents
- awesome-rag: https://github.com/asdfgh12345123/awesome-rag

### 个人主页仓库
- asdfgh12345123: https://github.com/asdfgh12345123/asdfgh12345123

## 3. 当前线上地址

- 主站: https://asdfgh12345123.github.io/awesome-ai-tools/
- Ko-fi: https://ko-fi.com/aitoolshub
- 爱发电: https://ifdian.net/a/aitoolshub

## 4. 本地路径（本次工作区）

- C:\Users\lyh\Documents\New project 3\awesome-ai-tools
- C:\Users\lyh\Documents\New project 3\awesome-ai-agents
- C:\Users\lyh\Documents\New project 3\awesome-rag

## 5. 当前最新 commit hash

- awesome-ai-tools: `ee74e81`
- awesome-ai-agents: `32b0c17`
- awesome-rag: `7f608d7`

## 6. 已完成功能

### 主站
- 首页、Donate、Supporters、Dashboard 页面优化
- 数据驱动页面与生成脚本
- SEO guides 生成
- sitemap / stats 生成
- link checker
- FUNDING / CONTRIBUTING / ISSUE TEMPLATE / PR TEMPLATE / ROADMAP / CHANGELOG
- GitHub Actions 自动化体系
- 与 Agents / RAG 仓库互链

### Agents 仓库
- README 重排为主站入口之一
- FUNDING / index 页面统一
- 反向链接到主站 agents guide

### RAG 仓库
- README 重排为主站入口之一
- FUNDING / index 页面统一
- 反向链接到主站 RAG guide

## 7. GitHub Actions 状态

主站仓库 workflow：
- `.github/workflows/build-site.yml`
- `.github/workflows/link-check.yml`
- `.github/workflows/seo-refresh.yml`
- `.github/workflows/weekly-digest.yml`
- `.github/workflows/update-stars.yml`
- `.github/workflows/deploy-pages.yml`（仅 manual）
- `.github/workflows/kofi-webhook.yml`（仅 manual）

## 8. 数据生成脚本

主站仓库脚本：
- `scripts/build_site.py`
- `scripts/generate_guides.py`
- `scripts/update_sitemap.py`
- `scripts/generate_stats.py`
- `scripts/generate_digest.py`
- `scripts/check_links.py`
- `.github/scripts/update_stars.py`

## 9. SEO 页面

当前主要 SEO/guide 页面包括：
- `guides/best-ai-tools-for-coding.html`
- `guides/best-ai-tools-for-writing.html`
- `guides/free-ai-tools.html`
- `guides/chatgpt-prompts-for-coding.html`
- `guides/chatgpt-prompts-for-writing.html`
- `guides/ai-agents-framework-comparison.html`
- `guides/rag-tools-comparison.html`

## 10. Ko-fi / 爱发电入口

三个仓库均已配置：
- README
- `.github/FUNDING.yml`
- 仓库 index 页面（如存在）

## 11. 仍需用户手动完成事项

- 撤销之前泄露过的旧 GitHub token
- 在 GitHub 确认 Pages 部署来源是否为 GitHub Actions
- 在 GitHub Actions 确认 `Build Site` 工作流运行成功
- 在 Google Search Console 提交 sitemap:
  - https://asdfgh12345123.github.io/awesome-ai-tools/sitemap.xml
- 完成爱发电认证所需的手动步骤

## 12. 后续建议

- 继续补齐真实工具和 prompt 数据量
- 统一更多页面的内部导航和 CTA
- 考虑把 Agents / RAG 仓库也接入轻量 Pages
- 在稳定后逐步增加社区提交内容

## 13. 风险提醒

- 本项目不保证收入、赞助转化或搜索排名
- 旧 token 泄露风险需要用户自行撤销
- 自动化 workflow 仍需关注 GitHub Actions 运行状态
- 如未来误触发重复部署，应检查 `build-site.yml` 与旧 `deploy-pages.yml`
