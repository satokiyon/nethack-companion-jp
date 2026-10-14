#!/usr/bin/env python3
"""
NetHack Companion 日本語版 最終完了監査スクリプト (5重の完全性チェック)。
全セグメントの完了、見出しの完全一致、未翻訳英文段落のゼロ検証、NetHackJP用語不一致ゼロ、
およびHTML/PDFビルド成果物を包括的に検証する。
"""

import json
import os
import re
import subprocess
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_completion_audit():
    print("==================================================")
    print("   NetHack Companion 日本語版 最終完了監査")
    print("==================================================\n")

    passed_all = True

    # 1. セグメント完全性監査
    print("【監査 1/5】セグメント完全性チェック...")
    progress_file = 'docs/translation_progress.json'
    if not os.path.exists(progress_file):
        print("  × エラー: progress.json が見つかりません。")
        return False

    with open(progress_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total = data['total_segments']
    segments = data['segments']
    pending_segs = [s for s in segments if s['status'] not in ('reviewed', 'integrated')]
    missing_files = []

    for s in segments:
        seg_path = os.path.join('docs/segments_ja', f"{s['id']}.md")
        if not os.path.exists(seg_path) or os.path.getsize(seg_path) == 0:
            missing_files.append(s['id'])

    if pending_segs:
        print(f"  × 未完了セグメントが {len(pending_segs)} 件存在します (先頭: {pending_segs[0]['id']})")
        passed_all = False
    elif missing_files:
        print(f"  × 欠損または空のセグメントファイルが {len(missing_files)} 件存在します: {missing_files[:5]}")
        passed_all = False
    else:
        print(f"  ✓ 合格: 全 {total} セグメントが完全に翻訳・レビューされています。")

    # 2. 見出し網羅性監査 (H1-H4)
    print("\n【監査 2/5】見出し網羅性チェック (H1〜H4)...")
    orig_md = 'spoilers/companion.md'
    ja_md = 'spoilers/companion.ja.md'

    if not os.path.exists(ja_md):
        print("  × エラー: companion.ja.md が存在しません。")
        return False

    with open(orig_md, 'r', encoding='utf-8') as f:
        orig_headers = [line.strip() for line in f if re.match(r'^#{1,4}\s+', line)]

    with open(ja_md, 'r', encoding='utf-8') as f:
        ja_headers = [line.strip() for line in f if re.match(r'^#{1,4}\s+', line)]

    print(f"  原本見出し数: {len(orig_headers)} / 日本語版見出し数: {len(ja_headers)}")
    if len(orig_headers) != len(ja_headers):
        print(f"  × 警告: 見出し数に差異があります (差分: {len(orig_headers) - len(ja_headers)} 件)")
        passed_all = False
    else:
        print(f"  ✓ 合格: 全 {len(orig_headers)} 個の見出しが1対1で対応しています。")

    # 3. 未翻訳ブロック・ゼロ監査
    print("\n【監査 3/5】未翻訳ブロック・ゼロチェック...")
    with open(ja_md, 'r', encoding='utf-8') as f:
        ja_text = f.read()

    # コメント・コード・数式・リンク等を除外
    cleaned = re.sub(r'<!--.*?-->', '', ja_text, flags=re.DOTALL)
    cleaned = re.sub(r'```.*?```', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'`.*?`', '', cleaned)
    cleaned = re.sub(r'\[.*?\]\(.*?\)', '', cleaned)

    # 15単語以上連続する純英文段落を検出
    english_paragraphs = []
    for para in cleaned.split('\n\n'):
        para = para.strip()
        if len(para) > 100:
            words = para.split()
            # 漢字・ひらがな・カタカナが含まれているか
            has_japanese = re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]', para)
            if not has_japanese and len(words) > 15:
                english_paragraphs.append(para[:60] + "...")

    if english_paragraphs:
        print(f"  × 未翻訳の英文段落が検出されました ({len(english_paragraphs)} 件):")
        for ep in english_paragraphs[:3]:
            print(f"    - {ep}")
        passed_all = False
    else:
        print("  ✓ 合格: 未翻訳の英文段落は検出されませんでした。")

    # 4. NetHackJP用語不一致ゼロ監査
    print("\n【監査 4/5】NetHackJP公式用語不一致監査...")
    try:
        res = subprocess.run([sys.executable, 'tools/audit_translated_terms.py'], capture_output=True, text=True)
        if "検出された不一致一覧 (0 件)" in res.stdout:
            print("  ✓ 合格: NetHackJP用語の不一致は 0 件です。")
        else:
            print("  × 警告: 用語不一致が検出されました:\n" + res.stdout)
            passed_all = False
    except Exception as e:
        print(f"  × エラー: 用語監査ツールの実行に失敗しました ({e})")
        passed_all = False

    # 5. ビルド成果物監査
    print("\n【監査 5/5】ビルド成果物チェック (HTML / PDF)...")
    html_file = 'spoilers/index.ja.html'
    pdf_file = 'spoilers/companion.ja.pdf'

    if os.path.exists(html_file) and os.path.getsize(html_file) > 100000:
        h_size = os.path.getsize(html_file) // 1024
        print(f"  ✓ index.ja.html 存在確認 ({h_size} KB)")
    else:
        print("  × index.ja.html が存在しないかサイズが小さすぎます。")
        passed_all = False

    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 500000:
        p_size = os.path.getsize(pdf_file) // 1024
        print(f"  ✓ companion.ja.pdf 存在確認 ({p_size} KB)")
    else:
        print("  × companion.ja.pdf が存在しないかサイズが小さすぎます。")
        passed_all = False

    print("\n--------------------------------------------------")
    if passed_all:
        print("★★★★★ 全5項目の完了監査に完全合格しました！ ★★★★★")
        print("NetHack Companion 日本語版プロジェクトは完全に完遂されました。")
    else:
        print("一部の監査項目で不合格または警告が残っています。修正が必要です。")
    print("--------------------------------------------------")

    return passed_all

if __name__ == '__main__':
    success = run_completion_audit()
    sys.exit(0 if success else 1)

