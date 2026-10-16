# -*- coding: utf-8 -*-
"""
Update Polymorph terminology across all Japanese segments.
Polymorph -> 変身(へんげ) / へんげ
Items:
  - WAN_POLYMORPH -> へんげの杖
  - POT_POLYMORPH -> へんげの薬
  - SCR_POLYMORPH -> へんげの巻物
  - SPE_POLYMORPH -> へんげの魔法書
  - RIN_POLYMORPH -> へんげの指輪
  - RIN_POLYMORPH_CONTROL -> へんげ制御の指輪 / へんげ制御
  - AMULET_OF_UNCHANGING -> 耐へんげの魔除け
  - RIN_PROTECTION_FROM_SHAPE_CHAN -> 耐へんげの指輪
General Polymorph action/trap/conduct -> 変身(へんげ)
"""
import os
import re

segments_dir = os.path.join("docs", "segments_jp")

replacements = [
    # Specific items
    ("変身の杖", "へんげの杖"),
    ("変身の薬", "へんげの薬"),
    ("変身の巻物", "へんげの巻物"),
    ("変身の魔法書", "へんげの魔法書"),
    ("変身の指輪", "へんげの指輪"),
    ("変身制御の指輪", "へんげ制御の指輪"),
    ("変身制御", "へんげ制御"),
    ("不変の魔除け", "耐へんげの魔除け"),
    ("変身生物除けの指輪", "耐へんげの指輪"),
    ("耐変身の魔除け", "耐へんげの魔除け"),
    ("耐変身の指輪", "耐へんげの指輪"),
    ("変身の罠", "変身(へんげ)の罠"),
    ("変身の呪文", "へんげの呪文"),
    ("変身ビーム", "変身(へんげ)ビーム"),
    ("自己変身なし", "自己変身(へんげ)なし"),
    ("アイテム変身なし", "アイテム変身(へんげ)なし"),
    ("変身制限", "変身(へんげ)制限"),
    # General Polymorph references
    ("変身（Polymorph）", "変身(へんげ) (Polymorph)"),
    ("変身 (Polymorph)", "変身(へんげ) (Polymorph)"),
    ("変身(Polymorph)", "変身(へんげ) (Polymorph)"),
    ("ポリモルフ", "変身(へんげ)"),
]

updated_files = []

for fname in os.listdir(segments_dir):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(segments_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    for target, repl in replacements:
        content = content.replace(target, repl)
    
    # Specific targeted edits
    if fname == "step_297.md":
        # Spell table: polymorph
        content = content.replace("| 変身 (polymorph) | 物質操作 | 6 | 方向指定 | 対象を変身させる |",
                                "| へんげ (polymorph) | 物質操作 | 6 | 方向指定 | 対象を変身(へんげ)させる |")
    
    if fname == "step_360.md":
        # Intrinsics: Polymorph control & Unchanging
        content = content.replace("**変身制御** (Polymorph control) | 罠、指輪、薬、杖、呪文によって変身する際、変身後の姿を自由に選択できる。 | なし。 | 変身制御の指輪。",
                                "**へんげ制御** (Polymorph control) | 罠、指輪、薬、杖、呪文によって変身(へんげ)する際、その姿を自由に選択できる。 | なし。 | へんげ制御の指輪。")
        content = content.replace("**不変** (Unchanging) | 現在の姿を固定する。あらゆる変身を防ぎ、*緑スライム化のカウントダウンも停止させる*。「スライムに触られた」際の標準的対処法。 | なし。 | 耐へんげの魔除け。",
                                "**耐へんげ** (Unchanging) | 現在の姿を固定する。あらゆる変身(へんげ)を防ぎ、*緑スライム化のカウントダウンも停止させる*。「スライムに触られた」際の標準的対処法。 | なし。 | 耐へんげの魔除け。")
        content = content.replace("**耐へんげの指輪** | 周囲のカメレオン、ドッペルゲンガー、サキュバス等の変身能力を封じる。",
                                "**耐へんげの指輪** (Protection from shape changers) | 周囲のカメレオン、ドッペルゲンガー、サキュバス等の変身能力を封じる。")

    if fname == "step_340.md":
        # Genetic engineer
        content = content.replace("プレイヤーを変身（ポリモルフ）させます。耐へんげの魔除けや魔法防御がなければ、一撃で別の生物に変えられてしまいます。",
                                "プレイヤーを変身(へんげ)させます。耐へんげの魔除けや魔法防御がなければ、一撃で別の生物に変身(へんげ)させられてしまいます。")

    if fname == "step_363.md":
        content = content.replace("祝福された変身(へんげ)の薬は、その1回の変身(へんげ)において変身先を自由に制御（選択）できます。",
                                "祝福されたへんげの薬は、その1回の変身(へんげ)において変身先を自由に制御（選択）できます。")

    if fname == "step_249.md":
        content = content.replace("### 変身制限 (Polyselfless & Polyobjectless)",
                                "### 変身(へんげ)制限 (Polyselfless & Polyobjectless)")

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files.append(fname)

print(f"Updated {len(updated_files)} files: {updated_files}")

