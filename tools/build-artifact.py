#!/usr/bin/env python3
"""Genera la versione da pubblicare come Artifact partendo da index.html.

L'Artifact avvolge il file in uno scheletro <!doctype><html><head>..</head><body>,
quindi qui teniamo solo <title>, il <link> dei font, lo <style> e il contenuto
del <body>. index.html resta l'unica fonte di verita'.
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
dst = Path(sys.argv[2] if len(sys.argv) > 2 else "build/artifact.html")
html = src.read_text(encoding="utf-8")


def grab(pattern):
    m = re.search(pattern, html, re.S | re.I)
    if not m:
        sys.exit(f"non trovo {pattern} in {src}")
    return m.group(0).strip()


title = grab(r"<title>.*?</title>")
fonts = grab(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>')
style = grab(r"<style>.*?</style>")
body = grab(r"<body[^>]*>.*?</body>")
body = re.sub(r"^<body[^>]*>|</body>$", "", body, flags=re.I).strip()

dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text("\n".join([title, fonts, style, "", body, ""]), encoding="utf-8")
print(f"{dst}: {len(dst.read_text(encoding='utf-8'))} byte")
