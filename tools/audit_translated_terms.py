#!/usr/bin/env python3
"""
NetHackJP（mon_jp.txt, obj_jp.txt, spell_jp.c, obj_jp.c）の公式定訳と、
現在翻訳済みの step_001.md 〜 step_012.md のテキストを徹底的に照合し、
不一致・誤訳・表記揺れを一覧化する監査スクリプト。
"""

import glob
import os
import re
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def load_master_glossary():
    glossary = {}

    # 1. mon_jp.txt
    mon_file = 'docs/glossary_references/mon_jp.txt'
    if os.path.exists(mon_file):
        with open(mon_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and ':' in line:
                    en, ja = line.split(':', 1)
                    glossary[en.strip().lower()] = (en.strip(), ja.strip(), 'モンスター')

    # 2. obj_jp.txt
    obj_file = 'docs/glossary_references/obj_jp.txt'
    if os.path.exists(obj_file):
        with open(obj_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and ':' in line:
                    en, ja = line.split(':', 1)
                    glossary[en.strip().lower()] = (en.strip(), ja.strip(), 'アイテム')

    # 3. spell_jp.c (NetHackJP)
    spell_c = r'C:\Users\satok\NetHackJP\src\spell_jp.c'
    if os.path.exists(spell_c):
        with open(spell_c, 'r', encoding='utf-8') as f:
            for line in f:
                # e.g. [SPE_FORCE_BOLT] = "衝撃",
                m = re.search(r'\[SPE_([A-Z_]+)\]\s*=\s*"([^"]+)"', line)
                if m:
                    const_name = m.group(1).lower().replace('_', ' ')
                    ja = m.group(2)
                    glossary[const_name] = (m.group(1), ja, '呪文')
                    # 別名マッピング (force bolt, magic mapping, sleep, healing, extra healing, etc.)
                    if const_name == 'force bolt':
                        glossary['force bolt'] = ('force bolt', ja, '呪文')
                    elif const_name == 'magic mapping':
                        glossary['magic mapping'] = ('magic mapping', ja, '呪文')

    # 4. artilist in obj_jp.c
    obj_c = r'C:\Users\satok\NetHackJP\src\obj_jp.c'
    if os.path.exists(obj_c):
        with open(obj_c, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        in_main_art = False
        for line in lines:
            if 'artilist_jp_names[' in line:
                in_main_art = True
            elif 'artilist_jnethack_names[' in line:
                in_main_art = False
            if in_main_art:
                m = re.search(r'\[ART_([A-Z_]+)\]\s*=\s*"([^"]+)"', line)
                if m:
                    art_key = m.group(1).lower().replace('_', ' ')
                    glossary[art_key] = (m.group(1), m.group(2), 'アーティファクト')
                    if art_key == 'excalibur':
                        glossary['excalibur'] = ('Excalibur', m.group(2), 'アーティファクト')
                    elif art_key == 'mjollnir':
                        glossary['mjollnir'] = ('Mjollnir', m.group(2), 'アーティファクト')
                    elif art_key == 'demonbane':
                        glossary['demonbane'] = ('Demonbane', m.group(2), 'アーティファクト')

    # 5. docs/glossary_custom.txt
    custom_file = 'docs/glossary_custom.txt'
    if os.path.exists(custom_file):
        with open(custom_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and ':' in line:
                    en, ja = line.split(':', 1)
                    en = en.strip()
                    ja = ja.strip()
                    glossary[en.lower()] = (en, ja, 'カスタム辞書')

    return glossary

def audit_segments():
    glossary = load_master_glossary()
    segment_files = sorted(glob.glob('docs/segments_jp/step_*.md'))

    print(f"マスター辞書エントリ数: {len(glossary)}")
    print(f"検査対象セグメント数: {len(segment_files)}\n")

    discrepancies = []

    for fpath in segment_files:
        seg_id = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # HTMLコメントを除外
        content_no_comments = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

        # 本文中の「日本語訳 (English)」または「日本語訳 (English / Other)」のパターンを抽出
        # e.g. 浮遊する目 (floating eye), 水の精 (water nymph), 魔法耐性のクローク (cloak of magic resistance)
        pattern = r'([^\s（(【「『\n]+)\s*\(([A-Za-z0-9\s,\'-\./]+)\)'
        matches = re.findall(pattern, content_no_comments)

        for ja_text, en_text in matches:
            # 英語部分をクリーンアップ
            en_clean = en_text.strip().lower()
            # 複合キーを分割して検査 (e.g. "wand of sleep" -> "wand of sleep")
            for candidate in [en_clean] + [part.strip() for part in re.split(r'[,/]', en_clean)]:
                if candidate in glossary:
                    orig_en, correct_ja, category = glossary[candidate]
                    # 訳語が一致しているか？
                    # ja_text に correct_ja が含まれているか、または完全一致するか
                    if correct_ja not in ja_text:
                        discrepancies.append({
                            'segment': seg_id,
                            'category': category,
                            'english': orig_en,
                            'current_ja': ja_text,
                            'correct_ja': correct_ja,
                            'context': f"{ja_text} ({en_text})"
                        })

    # 重複除去して整理
    unique_disc = {}
    for d in discrepancies:
        key = (d['category'], d['english'], d['current_ja'], d['correct_ja'])
        if key not in unique_disc:
            unique_disc[key] = []
        unique_disc[key].append(d['segment'])

    print(f"=== 検出された不一致一覧 ({len(unique_disc)} 件) ===")
    for (cat, en, cur_ja, cor_ja), segs in unique_disc.items():
        print(f"[{cat}] {en}")
        print(f"  現行訳: {cur_ja}")
        print(f"  公式訳 (NetHackJP): {cor_ja}")
        print(f"  出現箇所: {', '.join(set(segs))}\n")

if __name__ == '__main__':
    audit_segments()

