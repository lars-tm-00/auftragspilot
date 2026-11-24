"""Builds all generated subpages (DE + EN), llms.txt, agenten.md and sitemap.xml. Run from anywhere:
python3 _build/build_pages.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import agents  # noqa: E402
import common  # noqa: E402

MODULES = [agents]
for name in ("pages", "blog"):
    try:
        MODULES.append(__import__(name))
    except ModuleNotFoundError:
        pass

for m in MODULES:
    m.build()
common.sitemap()
print(len(common.PAGES), "pages")
