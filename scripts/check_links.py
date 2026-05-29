#!/usr/bin/env python3
import os, re

IGNORE_PREFIXES = ('http://', 'https://', 'mailto:', 'javascript:', 'tel:', 'data:')
TEMPLATE_EXPR = re.compile(r'^\$\{.*\}$|^\{\{.*\}$|^%[^%]+%$|^__\w+__$')


def normalize_local(href):
    href = href.split('#')[0].split('?')[0].strip()
    if not href or href == '.' or href == '..':
        return None
    if TEMPLATE_EXPR.match(href):
        return None
    if href.startswith(IGNORE_PREFIXES):
        return None
    if href.startswith('#'):
        return None
    if '${' in href or '{{' in href or '%5B' in href:
        return None
    if href.startswith('/'):
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
