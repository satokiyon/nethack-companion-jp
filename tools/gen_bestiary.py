# -*- coding: utf-8 -*-
"""
Generate Bestiary segments (step_298 to step_354).
Uses mon_jp.txt glossary and strict NetHackJP translation rules.
"""
import os
import re

# Load mon_jp.txt
glossary = {}
with open(os.path.join("docs", "glossary_references", "mon_jp.txt"), "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            en, ja = line.split(":", 1)
            glossary[en.strip().lower()] = ja.strip()

# Absolute overrides
glossary["floating eye"] = "さまよう目"
glossary["water nymph"] = "水のニンフ"
glossary["wood nymph"] = "森のニンフ"
glossary["mountain nymph"] = "山のニンフ"

def translate_mon_name(en_name):
    clean = en_name.strip()
    # Check if there is an alias like "knife (shito)" or similar
    lower = clean.lower()
    if lower in glossary:
        return f"{glossary[lower]} ({clean})"
    return clean

# Read companion.md
with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
    orig_lines = f.readlines()

import json
with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
    progress_data = json.load(f)

# Helper to map colors
colors_map = {
    "brown": "茶色",
    "yellow": "黄色",
    "blue": "青色",
    "red": "赤色",
    "black": "黒色",
    "magenta": "赤紫",
    "green": "緑色",
    "white": "白色",
    "cyan": "水色",
    "gray": "灰色",
    "grey": "灰色",
    "bright-blue": "明青",
    "bright-cyan": "明水",
    "bright-green": "明緑",
    "bright-magenta": "明紫",
    "orange": "橙色",
}

print(f"Loaded {len(glossary)} glossary terms.")

