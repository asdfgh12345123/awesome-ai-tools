#!/usr/bin/env python3
import os
from datetime import datetime

BASE_URL = 'https://asdfgh12345123.github.io/awesome-ai-tools'

def main():
    print('Generating sitemap...')
    urls = []
    for root, dirs, files in os.walk('.'):
        skip = set(root.split(os.sep))
        if skip & {'.git', 'private-products', 'dist', 'node_modules'}:
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, '.').replace('\\', '/')
            if rel.endswith('/index.html'):
                url = rel[:-len('index.html')]
            elif rel == 'index.html':
                url = ''
            else:
                url = rel[:-len('.html')]
            mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d')
            full = f'{BASE_URL}/{url}' if url else f'{BASE_URL}/'
            urls.append((full, mtime))

    urls = sorted(set(urls))
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        xml.append(f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>')
    xml.append('</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml) + '\n')
    print(f'Generated sitemap with {len(urls)} URLs')

if __name__ == '__main__':
    main()
