#!/usr/bin/env python3
"""
NetHack Companion 自律翻訳・進捗管理ユーティリティ。
各セグメントの原文抽出、進捗更新、訳文マージ、整合性チェックを行う。
"""

import json
import os
import re
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROGRESS_FILE = 'docs/translation_progress.json'
ORIG_MD = 'spoilers/companion.md'
JA_MD = 'spoilers/companion.ja.md'
REVIEW_NOTES = 'docs/translation_review_notes.md'

def load_progress():
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_progress(data):
    # 集計値を更新
    completed = len([s for s in data['segments'] if s['status'] in ('reviewed', 'integrated')])
    data['completed_segments'] = completed
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_next_pending():
    data = load_progress()
    for s in data['segments']:
        if s['status'] == 'pending':
            return s
    return None

def get_segment_source(seg):
    with open(ORIG_MD, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    start = seg['start_line'] - 1
    end = seg['end_line']
    return "".join(lines[start:end])

def update_segment_status(seg_id, status, notes=""):
    data = load_progress()
    for s in data['segments']:
        if s['id'] == seg_id:
            s['status'] = status
            if notes:
                s['notes'] = notes
            break
    save_progress(data)

def append_review_note(pattern, before, after, reason):
    entry = f"\n- **{pattern}**: `{before}` → `{after}` ({reason})"
    with open(REVIEW_NOTES, 'a', encoding='utf-8') as f:
        f.write(entry)

def print_status():
    data = load_progress()
    total = data['total_segments']
    done = data['completed_segments']
    pct = (done / total * 100) if total > 0 else 0
    print(f"進捗状況: {done}/{total} セグメント完了 ({pct:.1f}%)")

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'status':
        print_status()
    elif cmd == 'next':
        nxt = get_next_pending()
        if nxt:
            print(f"Next: [{nxt['id']}] {nxt['part']} > {nxt['section']} > {nxt['title']} (L{nxt['start_line']}-L{nxt['end_line']})")
        else:
            print("すべてのセグメントが完了しています！")
    elif cmd == 'source':
        seg_id = sys.argv[2]
        data = load_progress()
        for s in data['segments']:
            if s['id'] == seg_id:
                print(get_segment_source(s))
                break

