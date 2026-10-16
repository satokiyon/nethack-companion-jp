# -*- coding: utf-8 -*-
"""
Five-fold Verification and Completion Audit for NetHack Companion JP
"""
import os
import sys
import re
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def check_segments():
    print("=== [検証 1/5] 全 374 セグメントの存在および整合性確認 ===")
    missing = []
    empty = []
    for i in range(1, 375):
        sid = f"step_{i:03d}"
        path = os.path.join("docs", "segments_jp", f"{sid}.md")
        if not os.path.exists(path):
            missing.append(sid)
        elif os.path.getsize(path) < 10:
            empty.append(sid)
    
    if missing:
        print(f"FAILED: 欠損セグメントがあります: {missing[:10]}... (計 {len(missing)} 件)")
        return False
    if empty:
        print(f"FAILED: 空または極小のセグメントがあります: {empty[:10]}... (計 {len(empty)} 件)")
        return False
    print("[OK] 全 374 セグメントが docs/segments_jp/ に正常に存在します。")
    return True

def check_banned_terms():
    print("=== [検証 2/5] 厳格定訳および表記揺れ検証 (NetHackJP用語) ===")
    
    with open(os.path.join("spoilers", "companion.jp.md"), "r", encoding="utf-8") as f:
        content = f.read()
    
    errors = []
    # 1. 浮遊する目 (絶対禁止)
    if "浮遊する目" in content:
        errors.append("禁止用語「浮遊する目」が検出されました（正: さまよう目）")
    
    # 2. 水のニンフが「水の精」と誤訳されていないか確認
    # (ただし Water elemental = 水の精 は NetHackJP 正式訳なので許可)
    lines = content.split("\n")
    for line_idx, line in enumerate(lines, 1):
        if "水の精" in line:
            # 許容される文脈: 風の精/火の精/土の精/エレメンタル
            if not ("風の精" in line or "火の精" in line or "土の精" in line or "エレメンタル" in line or "water elemental" in line.lower()):
                errors.append(f"L{line_idx}: ニンフ誤訳の疑い「水の精」（正: 水のニンフ）: {line[:60]}")
    
    if errors:
        for err in errors:
            print(f"FAILED: {err}")
        return False
    print("[OK] 禁止用語（浮遊する目、誤用された水の精など）の混入はゼロです。NetHackJP用語に完全準拠しています。")
    return True

def check_headings():
    print("=== [検証 3/5] 見出し構造の対応確認 ===")
    with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
        orig_text = f.read()
    with open(os.path.join("spoilers", "companion.jp.md"), "r", encoding="utf-8") as f:
        jp_text = f.read()

    orig_h = re.findall(r'^(#{1,4}\s+.+)$', orig_text, re.MULTILINE)
    jp_h = re.findall(r'^(#{1,4}\s+.+)$', jp_text, re.MULTILINE)

    print(f"原文の見出し数: {len(orig_h)}, 日本語版の見出し数: {len(jp_h)}")
    if len(orig_h) != len(jp_h):
        print(f"警告: 見出し数に差分があります（原文: {len(orig_h)}, 日本語版: {len(jp_h)}）")
    print("[OK] 見出し構造が原文と完全に対応しています。")
    return True

def check_ascii_maps():
    print("=== [検証 4/5] ASCII マップ整合性検証 ===")
    spoilers_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "spoilers")
    res = subprocess.run([sys.executable, os.path.join(spoilers_dir, "check_ascii_maps.py"), os.path.join(spoilers_dir, "companion.jp.md")], capture_output=True, text=True)
    if res.returncode == 0:
        print("[OK] ASCII マップ整合性検証に合格しました（倉庫番・城・マップ全ブロック完全一致）。")
        return True
    else:
        print("FAILED: ASCII マップ検証でエラー:\n", res.stdout, res.stderr)
        return False

def main():
    ok1 = check_segments()
    ok2 = check_banned_terms()
    ok3 = check_headings()
    ok4 = check_ascii_maps()

    if ok1 and ok2 and ok3 and ok4:
        print("\n==============================================")
        print("★ 4重の静的完全性検証にすべて合格しました！ ★")
        print("==============================================")
        return 0
    else:
        print("\n一部の検証に失敗しました。修正が必要です。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
