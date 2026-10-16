#!/usr/bin/env python3
"""
本家リポジトリ (upstream) の更新を検知し、companion.md の差分が
どのセグメント（step_XXX）に影響するかを特定・報告するツール。
"""

import json
import os
import subprocess
import sys

# Windows コンソールでの文字化け・UnicodeEncodeError防止
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def check_upstream_diff(progress_json='docs/translation_progress.json', upstream_branch='upstream/main'):
    print(f"=== upstream 差分チェック ({upstream_branch} vs HEAD) ===")
    
    # git fetch upstream
    try:
        subprocess.run(['git', 'fetch', 'upstream'], check=True, capture_output=True, text=True)
        print("✓ upstream リモートから最新情報を取得しました。")
    except Exception as e:
        print(f"警告: git fetch upstream に失敗しました ({e})。ローカルキャッシュで比較します。")

    # git diff spoilers/companion.md
    cmd = ['git', 'diff', '--unified=0', 'HEAD', upstream_branch, '--', 'spoilers/companion.md']
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if res.returncode != 0:
        print(f"エラー: git diff に失敗しました: {res.stderr}")
        return

    diff_text = res.stdout.strip()
    if not diff_text:
        print("✓ 本家 (upstream) との差分はありません。最新状態に追従しています。")
        return

    print("\n[!] 本家 companion.md に変更を検出しました:")
    
    # 変更のあった行番号を抽出 (@@ -start,count +start,count @@)
    import re
    changed_lines = set()
    for line in diff_text.splitlines():
        if line.startswith('@@'):
            m = re.search(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
            if m:
                start = int(m.group(1))
                count = int(m.group(2)) if m.group(2) else 1
                for l in range(start, start + count):
                    changed_lines.add(l)

    print(f"変更行数: {len(changed_lines)} 行")

    # progress.json と照合して影響を受けるセグメントを特定
    with open(progress_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    affected_segments = []
    for seg in data.get('segments', []):
        s_line = seg['start_line']
        e_line = seg['end_line']
        if any(s_line <= cl <= e_line for cl in changed_lines):
            affected_segments.append(seg)

    print(f"\n影響を受けるセグメント ({len(affected_segments)} 件):")
    for s in affected_segments:
        print(f" - [{s['id']}] L{s['start_line']}-L{s['end_line']}: {s['part']} > {s['section']} > {s['title']}")

    print("\n次のアクション:")
    print(" 1. 上記セグメントの status を 'pending' に戻して差分翻訳を実施")
    print(" 2. レビュー後に companion.jp.md を更新")

if __name__ == '__main__':
    branch = sys.argv[1] if len(sys.argv) > 1 else 'upstream/main'
    check_upstream_diff(upstream_branch=branch)
