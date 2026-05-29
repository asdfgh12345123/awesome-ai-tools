#!/usr/bin/env python3
"""Generate paid product zip from private-products directory."""
import os
import zipfile
import re
import argparse

PRIVATE_DIR = 'private-products'
DIST_DIR = 'dist/private'

DANGEROUS_PATTERNS = [
    r'sk-[A-Za-z0-9]{20,}',
    r'ghp_[A-Za-z0-9]{36}',
    r'github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59}',
    r'xoxb-[0-9]{10,}-[A-Za-z0-9]{20,}',
    r'AKIA[0-9A-Z]{16}',
]


def check_file_for_secrets(filepath, content):
    issues = []
    for pattern in DANGEROUS_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            for match in matches:
                idx = content.find(match)
                context = content[max(0, idx-50):idx+len(match)+50]
                if any(x in context.lower() for x in ['example', 'placeholder', 'your-', 'xxx', '000', 'scan', 'pattern', 'check for']):
                    issues.append(f"WARNING: Possible example secret in {filepath}: {match[:10]}... (review manually)")
                else:
                    issues.append(f"ERROR: Real secret found in {filepath}: {match[:10]}...")
    return issues


def build_zip(product_name, version):
    source_dir = os.path.join(PRIVATE_DIR, product_name)
    
    if not os.path.exists(source_dir):
        print(f"ERROR: Source directory not found: {source_dir}")
        return False
    
    os.makedirs(DIST_DIR, exist_ok=True)
    zip_name = f"Codex-Automation-Starter-Kit-Pro-{version}.zip"
    zip_path = os.path.join(DIST_DIR, zip_name)
    
    print(f"Building {zip_path}...")
    
    all_issues = []
    file_count = 0
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            for f in files:
                if f.startswith('.') or f.endswith('.pyc'):
                    continue
                filepath = os.path.join(root, f)
                arcname = os.path.relpath(filepath, source_dir)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                        content = file_obj.read()
                    issues = check_file_for_secrets(filepath, content)
                    if issues:
                        all_issues.extend(issues)
                        if any('ERROR:' in i for i in issues):
                            print("ABORTED: Real secrets found in files!")
                            for issue in issues:
                                print(f"  {issue}")
                            if os.path.exists(zip_path):
                                os.remove(zip_path)
                            return False
                except Exception:
                    pass
                zf.write(filepath, arcname)
                file_count += 1
                print(f"  Added: {arcname}")
    
    size = os.path.getsize(zip_path)
    print(f"\nCreated {zip_path}")
    print(f"Files: {file_count}")
    print(f"Size: {size} bytes ({size / 1024:.1f} KB)")
    
    if all_issues:
        print("\nWarnings (review manually):")
        for issue in all_issues:
            print(f"  {issue}")
    
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', default='v1.0', help='Version string')
    parser.add_argument('--validate-only', action='store_true', help='Only validate, do not create zip')
    parser.add_argument('--path', default='codex-automation-starter-kit-pro', help='Product directory name')
    args = parser.parse_args()
    
    if args.validate_only:
        print("Validation mode - checking for secrets...")
        source_dir = os.path.join(PRIVATE_DIR, args.path)
        if not os.path.exists(source_dir):
            print(f"ERROR: Source directory not found: {source_dir}")
            exit(1)
        all_issues = []
        for root, dirs, files in os.walk(source_dir):
            for f in files:
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fo:
                        content = fo.read()
                    issues = check_file_for_secrets(filepath, content)
                    all_issues.extend(issues)
                except:
                    pass
        if all_issues:
            print("Issues found:")
            for i in all_issues:
                print(f"  {i}")
        else:
            print("No issues found.")
    else:
        build_zip(args.path, args.version)
