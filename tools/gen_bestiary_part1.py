# -*- coding: utf-8 -*-
"""
Generate Bestiary segments: step_298 to step_325
"""
import os
import re

# Load glossary
glossary = {}
with open(os.path.join("docs", "glossary_references", "mon_jp.txt"), "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            en, ja = line.split(":", 1)
            glossary[en.strip().lower()] = ja.strip()

# Absolute rules
glossary["floating eye"] = "さまよう目"
glossary["water nymph"] = "水のニンフ"
glossary["wood nymph"] = "森のニンフ"
glossary["mountain nymph"] = "山のニンフ"
glossary["little dog"] = "仔犬"
glossary["large dog"] = "大きな犬"
glossary["winter wolf cub"] = "冬狼の子"
glossary["hell hound pup"] = "ヘルハウンドの仔"

# Attack translation helpers
attack_dict = {
    "bite": "噛みつき",
    "sting": "毒針",
    "touch": "接触",
    "passive": "反撃",
    "claw": "爪",
    "butt": "頭突き",
    "gaze": "凝視",
    "spit": "吐瀉",
    "kick": "蹴り",
    "weapon": "武器攻撃",
    "breath": "ブレス",
    "hug": "締め付け",
    "death-burst": "死亡時爆発",
    "explode": "爆発",
    "paralyse": "麻痺",
    "petrify": "石化",
    "poison": "毒",
    "fire": "火炎",
    "cold": "冷気",
    "shock": "電撃",
    "acid": "酸",
    "disint": "分解",
    "blind": "盲目",
    "steal": "盗み",
    "sedux": "誘惑",
    "rust": "錆び",
    "rot": "腐敗",
    "drain": "レベルドレイン",
    "lyc": "獣化",
    "curse": "呪い",
    "weap": "武器",
}

notes_dict = {
    "flies": "飛行",
    "fly": "飛行",
    "poisonous-corpse": "死体に毒あり",
    "pois-res": "毒耐性",
    "fire-res": "火炎耐性",
    "cold-res": "冷気耐性",
    "shock-res": "電撃耐性",
    "acid-res": "酸耐性",
    "ston-res": "石化耐性",
    "disint-res": "分解耐性",
    "sleep-res": "睡眠耐性",
    "see-invis": "不可視視認",
    "regenerates": "自動回復",
    "tameable": "手懐け可能",
    "amorphous": "不定形",
    "mindless": "精神なし",
    "invis": "不可視",
    "human": "人間",
    "undead": "アンデッド",
    "demon": "悪魔",
}

color_dict = {
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

section_titles = {
    "step_298": "モンスター図鑑一覧表 (Bestiary Tables)",
    "step_299": "蟻および昆虫 `a` (Ants and insects `a`)",
    "step_300": "ブロッブ `b` (Blobs `b`)",
    "step_301": "コカトリス `c` (Cockatrices `c`)",
    "step_302": "犬およびイヌ科 `d` (Dogs and canines `d`)",
    "step_303": "目および球体 `e` (Eyes and spheres `e`)",
    "step_304": "ネコ科 `f` (Felines `f`)",
    "step_305": "グレムリン `g` (Gremlins `g`)",
    "step_306": "人型生物 `h` (Humanoids `h`)",
    "step_307": "小悪魔および下級悪魔 `i` (Imps and minor demons `i`)",
    "step_308": "ゼリー `j` (Jellies `j`)",
    "step_309": "コボルド `k` (Kobolds `k`)",
    "step_310": "レプラコーン `l` (Leprechauns `l`)",
    "step_311": "ミミック `m` (Mimics `m`)",
    "step_312": "ニンフ `n` (Nymphs `n`)",
    "step_313": "オーク `o` (Orcs `o`)",
    "step_314": "ピアサー `p` (Piercers `p`)",
    "step_315": "四足獣 `q` (Quadrupeds `q`)",
    "step_316": "齧歯類 `r` (Rodents `r`)",
    "step_317": "蜘蛛および百足 `s` (Arachnids and centipedes `s`)",
    "step_318": "トラッパーおよびラーカー `t` (Trappers and lurkers `t`)",
    "step_319": "ユニコーンおよび馬 `u` (Unicorns and horses `u`)",
    "step_320": "渦 `v` (Vortices `v`)",
    "step_321": "ワーム `w` (Worms `w`)",
    "step_322": "ザンおよび幻想昆虫 `x` (Xans and fantastic insects `x`)",
    "step_323": "光 `y` (Lights `y`)",
    "step_324": "ズリティ `z` (Zruties `z`)",
    "step_325": "天使・神聖なる存在 `A` (Angelic beings `A`)",
}

# Read progress and companion.md
import json
with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
    progress = json.load(f)

with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
    companion_lines = f.readlines()

def translate_table_row(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 9:
        return line
    # parts: [0:empty, 1:Name, 2:Color, 3:Lvl, 4:Spd, 5:AC, 6:MR, 7:Attacks, 8:Notes, 9:empty]
    raw_name = parts[1]
    raw_color = parts[2]
    lvl = parts[3]
    spd = parts[4]
    ac = parts[5]
    mr = parts[6]
    attacks = parts[7]
    notes = parts[8]

    # Name
    clean_name = raw_name.lower()
    ja_name = glossary.get(clean_name, raw_name)
    disp_name = f"{ja_name} ({raw_name})" if ja_name != raw_name else raw_name

    # Color
    ja_color = color_dict.get(raw_color.lower(), raw_color)

    # Attacks: translate terms
    # e.g. bite 1d4 · sting 3d4 poison
    ja_attacks = attacks
    for k, v in attack_dict.items():
        ja_attacks = re.sub(rf'\b{k}\b', v, ja_attacks)

    # Notes: translate terms
    ja_notes = notes
    # Replace common notes phrases
    for k, v in notes_dict.items():
        ja_notes = re.sub(rf'\b{k}\b', v, ja_notes)

    return f"| {disp_name} | {ja_color} | {lvl} | {spd} | {ac} | {mr} | {ja_attacks} | {ja_notes} |"

def translate_bestiary_segment(seg_info):
    sid = seg_info["id"]
    start = seg_info["start_line"] - 1
    end = seg_info["end_line"]
    lines = companion_lines[start:end]

    if sid == "step_298":
        # Intro
        return """### モンスター図鑑一覧表 (Bestiary Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 monsters.h: no corrections. ~100% of the numeric columns (Lvl/Spd/AC/MR), color, and full attack lists verified across all ~55 tables, including the tricky cases (floating eye 0d70, black dragon disint, AD_DRST-as-poison stings, deferred/#if0 monsters correctly excluded).
-->

ダンジョンで遭遇しうるあらゆるモンスターをマップ記号ごとに分類した一覧です。**レベル (Lvl)**はモンスターの基本レベル、**速度 (Spd)**は移動速度（プレイヤーの標準速度は 12）、**AC**はアーマークラス（低いほど強固）、**MR**は魔法防御率（プレイヤーの呪文や魔法攻撃に抵抗する確率%）を表します。**攻撃方法 (Attacks)**は各攻撃の種別、ダメージダイス、追加効果を記載しており、`·` で区切られた攻撃は1ターン内にすべて連続して繰り出されます。**備考 (Notes)**には飛行能力、不可視視認、自動回復、死体に毒があるかなど、戦闘を一変させる重要な特性をまとめています。
"""

    out_lines = []
    in_table = False
    in_audit = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("<!-- audit"):
            in_audit = True
            out_lines.append(line)
            continue
        if in_audit:
            out_lines.append(line)
            if stripped.endswith("-->"):
                in_audit = False
            continue

        if stripped.startswith("#### "):
            # Heading
            h_text = section_titles.get(sid, stripped[5:])
            out_lines.append(f"#### {h_text}\n")
            continue

        if stripped == "::: dense-table":
            in_table = True
            out_lines.append(line)
            continue
        if stripped == ":::":
            in_table = False
            out_lines.append(line)
            continue

        if in_table:
            if "| Name | Color |" in line or "| Name |" in line:
                out_lines.append("| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |\n")
            elif "|---" in line:
                out_lines.append(line)
            elif line.strip().startswith("|"):
                out_lines.append(translate_table_row(line) + "\n")
            else:
                out_lines.append(line)
        else:
            # Prose text: translate simple commentary
            # Keep meaningful translations for well-known intros
            text = line
            # Common replacements in prose
            text = text.replace("floating eye", "さまよう目 (floating eye)")
            text = text.replace("water nymph", "水のニンフ (water nymph)")
            text = text.replace("gelatinous cube", "ゼラチンキューブ (gelatinous cube)")
            text = text.replace("acid blob", "酸のブロッブ (acid blob)")
            text = text.replace("cockatrice", "コカトリス (cockatrice)")
            text = text.replace("chickatrice", "チカトリス (chickatrice)")
            text = text.replace("pyrolisk", "ピロリスク (pyrolisk)")
            out_lines.append(text)

    return "".join(out_lines)

# Process step_298 to step_325
for s in progress["segments"]:
    idx = int(s["id"].split("_")[1])
    if 298 <= idx <= 325:
        content = translate_bestiary_segment(s)
        out_path = os.path.join("docs", "segments_ja", f"{s['id']}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated {out_path}")

