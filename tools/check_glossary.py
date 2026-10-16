#!/usr/bin/env python3
"""
翻訳済みテキスト（または companion.jp.md 全体）に対して、
用語集（mon_jp.txt, obj_jp.txt, glossary_custom.txt）の適用状況や
Markdown構文（テーブル、コードブロック）の整合性を検証するツール。
"""

import os
import re
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def load_glossaries():
    glossary = {}
    
    files = [
        'docs/glossary_references/mon_jp.txt',
        'docs/glossary_references/obj_jp.txt',
        'docs/glossary_custom.txt'
    ]
    
    for fpath in files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    parts = line.split(':', 1)
                    en = parts[0].strip()
                    ja = parts[1].strip()
                    if en and ja:
                        glossary[en] = ja

    return glossary

def check_text(text, orig_text=""):
    glossary = load_glossaries()
    warnings = []

    # 1. コードブロック閉じチェック
    code_blocks = text.count('```')
    if code_blocks % 2 != 0:
        warnings.append("[構文エラー] コードブロック (```) が閉じていません。")

    # 2. テーブル整合性チェック（行ごとのパイプ数）
    if orig_text:
        orig_pipes = [line.count('|') for line in orig_text.splitlines() if '|' in line]
        ja_pipes = [line.count('|') for line in text.splitlines() if '|' in line]
        if len(orig_pipes) != len(ja_pipes):
            warnings.append(f"[テーブル警告] テーブル行数が原文と一致しません (原文: {len(orig_pipes)}行, 訳文: {len(ja_pipes)}行)")
        elif orig_pipes and ja_pipes:
            mismatches = [(i+1, o, j) for i, (o, j) in enumerate(zip(orig_pipes, ja_pipes)) if o != j]
            if mismatches:
                warnings.append(f"[テーブル警告] テーブル列数（パイプ数）の不整合があります: {mismatches[:3]}")

    # 3. 英語の丸残りチェック（英単語として単独で残っているモンスター・アイテム・重要語）
    # ただし (英語名) 併記は除外する
    cleaned = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL) # HTMLコメントを除外
    cleaned = re.sub(r'『[A-Za-z0-9\s,\'-\./]+』', '', cleaned) # 日本語書籍・ゲーム名表記を除外
    cleaned = re.sub(r'「[A-Za-z0-9\s,\'-\./]+」', '', cleaned)
    cleaned = re.sub(r'[（\(][^）\)]*?[A-Za-z]+[^）\)]*?[）\)]', '', cleaned) # 半角・全角カッコ内の英語併記を除外
    cleaned = re.sub(r'```.*?```', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'`.*?`', '', cleaned)
    cleaned = re.sub(r'\[.*?\]\(.*?\)', '', cleaned) # リンクURL

    # 単語境界でのマッチ
    detected_untranslated = []
    # 3文字以上の重要単語のみ抽出検査
    for en, ja in glossary.items():
        if len(en) < 4:
            continue
        # 英語名が文章中に単独（アルファベットで囲まれていない）で残っていないか
        pattern = r'\b' + re.escape(en) + r'\b'
        if re.search(pattern, cleaned, re.IGNORECASE):
            detected_untranslated.append((en, ja))

    if detected_untranslated:
        # 重複除去して上位5件を表示
        unique = list({en: ja for en, ja in detected_untranslated}.items())
        warnings.append(f"[用語警告] 未翻訳の英単語が検出されました (計{len(unique)}件): " + 
                        ", ".join([f"'{e}' -> '{j}'" for e, j in unique[:5]]))

    return warnings

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'spoilers/companion.jp.md'
    if os.path.exists(target):
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read()
        res = check_text(content)
        if res:
            print(f"=== {target} の検証警告 ===")
            for w in res:
                print(" - " + w)
        else:
            print(f"✓ {target}: 問題は検出されませんでした。")
    else:
        print(f"対象ファイルが見つかりません: {target}")

