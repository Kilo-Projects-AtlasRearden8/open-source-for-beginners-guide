#!/usr/bin/env python3
"""Verify the Open Source for Beginners project meets its requirements.

Run: python3 verify.py
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
ERRORS = []

COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"


def fail(msg):
    ERRORS.append(msg)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


# 1. Required files exist
required = [
    "LICENSE", "README.md", "STATUS.md", "verify.py",
    "docs/intro.md", "docs/finding-projects.md", "docs/installing.md",
    "docs/reporting-issues.md", "docs/first-pull-request.md", "docs/checklist.md",
    "static/index.html", "static/checklist.html", "static/style.css",
]
for path in required:
    if not os.path.exists(os.path.join(ROOT, path)):
        fail(f"Missing required file: {path}")

# 2. LICENSE exact copyright line (standalone line)
lic = read("LICENSE")
if COPYRIGHT not in lic:
    fail(f"LICENSE missing exact line: {COPYRIGHT}")
if f"\n{COPYRIGHT}\n" not in lic:
    fail(f"LICENSE copyright line is not standalone: {COPYRIGHT}")

# 3. README credits Asdale Dynamics, LLC
readme = read("README.md")
if "Asdale Dynamics, LLC" not in readme:
    fail("README.md does not credit Asdale Dynamics, LLC")

# 4. HTML files parse and contain required strings
for html in ["static/index.html", "static/checklist.html"]:
    content = read(html)
    parser = HTMLParser()
    try:
        parser.feed(content)
    except Exception as exc:  # noqa: BLE001
        fail(f"{html}: HTML parse error: {exc}")
    for s in ["Asdale Dynamics, LLC", COPYRIGHT, "MIT License"]:
        if s not in content:
            fail(f"{html} missing: {s}")

# 5. No .github/workflows
if os.path.exists(os.path.join(ROOT, ".github", "workflows")):
    fail(".github/workflows must not be present")

# 6. No secrets or personal data patterns in content files
secret_patterns = [
    r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"ghp_[A-Za-z0-9]{36,}",
    r"password\s*=\s*\S+",
    r"api[_-]?key\s*=\s*\S+",
]
content_files = [
    p for p in required if p != "verify.py"
]
for path in content_files:
    text = read(path)
    for pat in secret_patterns:
        if re.search(pat, text, re.IGNORECASE):
            fail(f"{path}: possible secret matched ({pat})")

if ERRORS:
    print("VERIFICATION FAILED:")
    for e in ERRORS:
        print(f"  - {e}")
    sys.exit(1)

print("VERIFICATION PASSED")
print(f"  Required files present: {len(required)}")
print(f"  LICENSE exact copyright line: OK")
print(f"  README credits Asdale Dynamics, LLC: OK")
print(f"  HTML files parse and credit LLC: OK")
print(f"  No .github/workflows: OK")
print(f"  No secrets detected: OK")
