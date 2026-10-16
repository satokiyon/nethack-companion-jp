#!/usr/bin/env python3
"""
docs/segments_jp/step_XXX.md を順次結合し、spoilers/companion.jp.md を生成するスクリプト。
"""

import json
import os
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def assemble(progress_json='docs/translation_progress.json', segments_dir='docs/segments_jp', output_md='spoilers/companion.jp.md'):
    with open(progress_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    
    parts = []
    missing = []
    total = len(data['segments'])

    for s in data['segments']:
        seg_id = s['id']
        seg_file = os.path.join(segments_dir, f"{seg_id}.md")
        if os.path.exists(seg_file):
            with open(seg_file, 'r', encoding='utf-8') as sf:
                parts.append(sf.read().rstrip())
        else:
            missing.append(seg_id)

    combined_text = "\n\n".join(parts) + "\n"
    
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(combined_text)

    assembled_count = len(parts)
    print(f"アセンブル完了: {assembled_count}/{total} セグメントを {output_md} に出力しました。")
    if missing:
        print(f"未アセンブルのセグメント: {len(missing)} 件 (先頭: {missing[0]})")

if __name__ == '__main__':
    assemble()

