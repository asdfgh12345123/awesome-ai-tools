# Windows Commands Reference

Common PowerShell and Git commands for project automation on Windows.

## Git basics

~~~powershell
git init

git status

git add .

git commit -m "your commit message"

git push origin main

git pull origin main

git remote -v
~~~

## Python scripts

~~~powershell
python scripts/build_site.py

python --version

python -m py_compile scripts/build_site.py
~~~

## GitHub CLI

~~~powershell
gh auth status

gh auth login

gh auth setup-git
~~~

## File operations

~~~powershell
Get-ChildItem -Recurse -Filter *.html

Get-Content data/tools.json
~~~

## Troubleshooting

~~~powershell
git config --list

git config user.name "Your Name"

git config user.email "your@email.com"
~~~
