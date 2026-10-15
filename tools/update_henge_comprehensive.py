# -*- coding: utf-8 -*-
"""
Comprehensive update for Polymorph -> 変身(へんげ) / へんげ
and related terms across all segments.
"""
import os
import re

segments_dir = os.path.join("docs", "segments_ja")

# Regex-based replacements for precision
rules = [
    # Headings
    (r"道具としてのポリモーフ \(Polymorph as a Tool\)", "道具としての変身(へんげ) (Polymorph as a Tool)"),
    (r"### 変身制限 \(Polyselfless & Polyobjectless\)", "### 変身(へんげ)制限 (Polyselfless & Polyobjectless)"),
    
    # Common noun/verb phrases
    (r"ポリモーフ（変身）", "変身(へんげ)"),
    (r"変身（ポリモルフ）", "変身(へんげ)"),
    (r"変身 \(ポリモルフ\)", "変身(へんげ)"),
    (r"変身\(ポリモルフ\)", "変身(へんげ)"),
    (r"ポリモルフ", "変身(へんげ)"),
    
    # Items
    (r"変身の杖", "へんげの杖"),
    (r"変身の薬", "へんげの薬"),
    (r"変身の巻物", "へんげの巻物"),
    (r"変身の魔法書", "へんげの魔法書"),
    (r"変身の指輪", "へんげの指輪"),
    (r"変身制御の指輪", "へんげ制御の指輪"),
    (r"変身制御", "へんげ制御"),
    (r"耐変身の魔除け", "耐へんげの魔除け"),
    (r"耐変身の指輪", "耐へんげの指輪"),
    (r"不変の魔除け", "耐へんげの魔除け"),
    (r"変身生物除けの指輪", "耐へんげの指輪"),
    
    # Actions & states
    (r"変身の罠", "変身(へんげ)の罠"),
    (r"変身の呪文", "へんげの呪文"),
    (r"変化の呪文", "へんげの呪文"),
    (r"変身ビーム", "変身(へんげ)ビーム"),
    (r"自己変身なし", "自己変身(へんげ)なし"),
    (r"アイテム変身なし", "アイテム変身(へんげ)なし"),
    (r"自己変身", "自己変身(へんげ)"),
    (r"変身ショック", "変身(へんげ)ショック"),
]

modified_files = []

for fname in sorted(os.listdir(segments_dir)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(segments_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for pattern, repl in rules:
        new_content = re.sub(pattern, repl, new_content)

    # Clean double parentheses if any e.g. 変身(へんげ)(へんげ)
    new_content = new_content.replace("変身(へんげ)(へんげ)", "変身(へんげ)")
    new_content = new_content.replace("変身(へんげ)(へんげ)", "変身(へんげ)")

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        modified_files.append(fname)

print(f"Applied comprehensive updates to {len(modified_files)} files: {modified_files}")

