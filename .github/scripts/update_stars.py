import os
import re
import urllib.request
import json

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
HEADERS = {'Accept': 'application/vnd.github+json', 'User-Agent': 'awesome-ai-tools-bot'}
if GITHUB_TOKEN:
    HEADERS['Authorization'] = f'Bearer {GITHUB_TOKEN}'


def get_stars(repo_name):
    url = f'https://api.github.com/repos/{repo_name}'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return int(data.get('stargazers_count', 0) or 0)
    except Exception as exc:
        print(f'WARNING: failed to fetch stars for {repo_name}: {exc}')
        return None


def main():
    readme = 'README.md'
    if not os.path.exists(readme):
        print('README.md not found')
        return

    with open(readme, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'\[([^\]]+)\]\(https://github\.com/([^/]+)/([^)]+)\)')
    seen = {}
    updated = 0

    def replace_match(m):
        nonlocal updated
        name = m.group(1)
        owner = m.group(2)
        repo = m.group(3).rstrip('/')
        repo_path = f'{owner}/{repo}'
        if repo_path not in seen:
            seen[repo_path] = get_stars(repo_path)
        stars = seen[repo_path]
        if stars is None:
            return m.group(0)
        if stars >= 1000:
            star_str = f'{stars // 1000}k+'
        else:
            star_str = str(stars)
        updated += 1
        return f'[{name}](https://github.com/{owner}/{repo})'

    new_content = pattern.sub(replace_match, content)
    if new_content != content:
        with open(readme, 'w', encoding='utf-8') as f:
            f.write(new_content)
    print(f'Processed repos: {len(seen)}, link refreshes: {updated}')


if __name__ == '__main__':
    main()
