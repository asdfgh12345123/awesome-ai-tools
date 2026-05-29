#!/usr/bin/env python3
"""Generate paid product zip from private-products directory."""
import os
import zipfile
import re

PRIVATE_DIR = 'private-products'
DIST_DIR = 'dist/private'

# Patterns that should NOT appear in files (actual secrets)
DANGEROUS_PATTERNS = [
    r'sk-[A-Za-z0-9]{20,}',  # OpenAI API key
    r'ghp_[A-Za-z0-9]{36}',  # GitHub personal access token
    r'github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59}',  # GitHub fine-grained token
    r'xoxb-[0-9]{10,}-[A-Za-z0-9]{20,}',  # Slack bot token
    r'AKIA[0-9A-Z]{16}',  # AWS access key
]

# Patterns that are OK in context (examples/documentation)
CONTEXT_PATTERNS = [
    'sk-*', 'ghp_*', 'Bearer tokens', 'api_key=', 'password=',
]


def check_file_for_secrets(filepath, content):
    """Check if file contains actual secrets (not just examples)."""
    issues = []
    
    for pattern in DANGEROUS_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            # Check if it's in a context that suggests it's an example
            for match in matches:
                # Look for surrounding context
                idx = content.find(match)
                context = content[max(0, idx-50):idx+len(match)+50]
                
                # If it's in a code block or mentioned as "example", it might be OK
                if any(x in context.lower() for x in ['example', 'placeholder', 'your-', 'xxx', '000']):
                    issues.append(f"WARNING: Possible example secret in {filepath}: {match[:10]}... (review manually)")
                else:
                    issues.append(f"ERROR: Real secret found in {filepath}: {match[:10]}...")
    
    return issues


def build_zip(product_name, version):
    """Build the paid product zip."""
    source_dir = os.path.join(PRIVATE_DIR, product_name)
    
    if not os.path.exists(source_dir):
        print(f"ERROR: Source directory not found: {source_dir}")
        print(f"Please create {source_dir} and add your Pro content files.")
        return False
    
    os.makedirs(DIST_DIR, exist_ok=True)
    zip_name = f"{product_name.replace('-pro', '').title().replace('-', '-')}-Pro-v{version}.zip"
    zip_path = os.path.join(DIST_DIR, zip_name)
    
    print(f"Building {zip_path}...")
    
    all_issues = []
    file_count = 0
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            # Skip hidden directories and __pycache__
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for f in files:
                # Skip hidden files and caches
                if f.startswith('.') or f.endswith('.pyc'):
                    continue
                
                filepath = os.path.join(root, f)
                arcname = os.path.relpath(filepath, source_dir)
                
                # Read and check content
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                        content = file_obj.read()
                    
                    issues = check_file_for_secrets(filepath, content)
                    if issues:
                        all_issues.extend(issues)
                        # If there's a real error (not just warning), stop
                        if any('ERROR:' in i for i in issues):
                            print("ABORTED: Real secrets found in files!")
                            for issue in issues:
                                print(f"  {issue}")
                            # Remove incomplete zip
                            if os.path.exists(zip_path):
                                os.remove(zip_path)
                            return False
                
                except Exception:
                    pass  # Binary files can't be read as text
                
                zf.write(filepath, arcname)
                file_count += 1
                print(f"  Added: {arcname}")
    
    print(f"\nCreated {zip_path}")
    print(f"Files: {file_count}")
    print(f"Size: {os.path.getsize(zip_path)} bytes ({os.path.getsize(zip_path) / 1024:.1f} KB)")
    
    if all_issues:
        print("\nWarnings (review manually):")
        for issue in all_issues:
            print(f"  {issue}")
    
    return True


if __name__ == '__main__':
    build_zip('codex-automation-starter-kit-pro', '1.0')
