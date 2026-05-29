#!/usr/bin/env python3
import os, re

def normalize_local(href):
    href = href.split('#')[0].split('?')[0]
    if href == '' or href == '.':
        return 'index.html'
    if href.startswith('/'):
        return None
    if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:') or href.startswith('javascript:'):
        return None
    if href.endswith('/'):
        return href + 'index.html'
    if not os.path.splitext(href)[1]:
        return href + '/index.html'
    return href

def check_file(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    for href in re.findall(r'href="([^"]+)"', html):
        local = normalize_local(href)
        if local is None:
            continue
        candidate = os.path.join(os.path.dirname(filepath), local)
        if not os.path.exists(candidate):
            issues.append(f'MISSING: {href} -> {os.path.relpath(candidate, ".")}')
    return issues

def main():
    print('Checking local links...')
    total = 0
    for root, dirs, files in os.walk('.'):
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            issues = check_file(path)
            if issues:
                total += len(issues)
                print(f'\n{path}:')
                for issue in issues:
                    print(issue)
    print(f'\nTotal local link issues: {total}')

if __name__ == '__main__':
    main()
