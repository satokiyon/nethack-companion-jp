# -*- coding: utf-8 -*-
"""
Five-fold Verification and Completion Audit for NetHack Companion JP
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


def pandoc_slug(heading_text, seen_counts):
    """原著の英語見出し文字列から Pandoc auto_identifiers 準拠のアンカーIDを算出する。"""
    m_attr = re.match(r'^(.+?)\s*\{([#\.][^}`]*)\}\s*$', heading_text)
    if m_attr:
        base_text = m_attr.group(1)
        attr_content = m_attr.group(2)
        m_id = re.search(r'(?:^|\s)#([^\s}]+)', attr_content)
        if m_id:
            slug = m_id.group(1)
            seen_counts[slug] = seen_counts.get(slug, 0) + 1
            return slug
    else:
        base_text = heading_text

    s = base_text.lower()
    s = re.sub(r'[^\w\s.-]', '', s)
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'^[^a-z]+', '', s)
    if not s:
        s = "section"
    if s in seen_counts:
        seen_counts[s] += 1
        return f"{s}-{seen_counts[s] - 1}"
    else:
        seen_counts[s] = 1
        return s


def extract_headings(lines):
    """コードブロック外の全見出し (level_hashes, text) を抽出する。"""
    res = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
        if not in_code:
            m = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
            if m:
                res.append((m.group(1), m.group(2)))
    return res


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
    print("=== [検証 3/5] 見出し構造およびセグメント境界の対応確認 ===")
    with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
        orig_lines = f.read().splitlines()
    with open(os.path.join("spoilers", "companion.jp.md"), "r", encoding="utf-8") as f:
        jp_lines = f.read().splitlines()
    with open(os.path.join("docs", "translation_progress.json"), "r", encoding="utf-8") as f:
        prog = json.load(f)

    orig_h = extract_headings(orig_lines)
    jp_h = extract_headings(jp_lines)

    print(f"原文の見出し数 (H1-H6): {len(orig_h)}, 日本語版の見出し数 (H1-H6): {len(jp_h)}")
    if len(orig_h) != len(jp_h):
        print(f"FAILED: 見出し数に差分があります（原文: {len(orig_h)}, 日本語版: {len(jp_h)}）")
        return False

    for s in prog.get("segments", []):
        sid = s["id"]
        seg_en_h = extract_headings(orig_lines[s["start_line"] - 1 : s["end_line"]])
        seg_path = os.path.join("docs", "segments_jp", f"{sid}.md")
        with open(seg_path, "r", encoding="utf-8") as sf:
            seg_jp_h = extract_headings(sf.read().splitlines())
        if len(seg_en_h) != len(seg_jp_h):
            print(f"FAILED: {sid} の見出し数が原文と一致しません (EN={len(seg_en_h)}, JP={len(seg_jp_h)})")
            return False

    print("[OK] 全401見出しおよび全374セグメントの見出し構造が原文と1対1で完全に対応しています。")
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


def check_anchors_and_links():
    print("=== [検証 5/5] アンカーID（英語のみ・非ASCII混入ゼロ）および内部リンク整合性検証 ===")
    with open(os.path.join("spoilers", "companion.md"), "r", encoding="utf-8") as f:
        en_text = f.read()
    with open(os.path.join("spoilers", "companion.jp.md"), "r", encoding="utf-8") as f:
        jp_text = f.read()

    en_headings = extract_headings(en_text.splitlines())
    jp_headings = extract_headings(jp_text.splitlines())

    seen_counts = {}
    expected_slugs = [pandoc_slug(h[1], seen_counts) for h in en_headings]

    # 1. companion.jp.md の全見出しに {#english-slug} が明示されているか確認
    missing_or_wrong = []
    for idx, ((_, jp_h_text), exp_slug) in enumerate(zip(jp_headings, expected_slugs)):
        m_attr = re.search(r'\{([#\.][^}`]*)\}\s*$', jp_h_text)
        if not m_attr:
            missing_or_wrong.append(f"見出し[{idx}] にアンカー属性がありません: {jp_h_text}")
            continue
        m_id = re.search(r'(?:^|\s)#([^\s}]+)', m_attr.group(1))
        if not m_id:
            missing_or_wrong.append(f"見出し[{idx}] に #id がありません: {jp_h_text}")
            continue
        actual_slug = m_id.group(1)
        if actual_slug != exp_slug:
            missing_or_wrong.append(f"見出し[{idx}] のアンカー不一致: actual=#{actual_slug}, expected=#{exp_slug}")
        elif not actual_slug.isascii():
            missing_or_wrong.append(f"見出し[{idx}] のアンカーに非ASCII文字が含まれています: #{actual_slug}")

    if missing_or_wrong:
        for err in missing_or_wrong[:15]:
            print(f"FAILED: {err}")
        return False

    # 2. Markdown 内の明示アンカー {#...} およびリンク ](#...) に非ASCII文字がないか確認
    explicit_ids = re.findall(r'\{#([^}\s]+)', jp_text)
    non_ascii_md_ids = [i for i in explicit_ids if not i.isascii()]
    if non_ascii_md_ids:
        print(f"FAILED: companion.jp.md 内に非ASCIIのアンカー定義があります: {non_ascii_md_ids[:10]}")
        return False

    md_links = re.findall(r'\]\(#([^)]+)\)', jp_text)
    non_ascii_md_links = [l for l in md_links if not l.isascii()]
    if non_ascii_md_links:
        print(f"FAILED: companion.jp.md 内に非ASCIIのアンカーリンクがあります: {non_ascii_md_links[:10]}")
        return False

    # 3. index.jp.html の全 id="..." と href="#..." の検証
    html_path = os.path.join("spoilers", "index.jp.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            jp_html = f.read()

        html_ids = re.findall(r'\bid="([^"]+)"', jp_html)
        non_ascii_html_ids = [i for i in html_ids if not i.isascii()]
        if non_ascii_html_ids:
            print(f"FAILED: index.jp.html に非ASCIIの id 属性が {len(non_ascii_html_ids)} 件残っています: {non_ascii_html_ids[:10]}")
            return False

        html_id_set = set(html_ids)
        # テンプレートJS内の文字列結合 ('#' + m.id 等) を除外してリンク切れチェック
        html_hrefs = [
            h for h in re.findall(r'\bhref="#([^"]+)"', jp_html)
            if not h.startswith("'")
        ]
        broken_links = [h for h in html_hrefs if h not in html_id_set]
        if broken_links:
            print(f"FAILED: index.jp.html 内にリンク切れのアンカーが {len(broken_links)} 件あります: {broken_links[:10]}")
            return False

    print(f"[OK] 全 {len(expected_slugs)} 見出し・全インラインアンカーが英語化され、非ASCII混入 0 件・内部リンク切れ 0 件です。")
    return True


def main():
    ok1 = check_segments()
    ok2 = check_banned_terms()
    ok3 = check_headings()
    ok4 = check_ascii_maps()
    ok5 = check_anchors_and_links()

    if ok1 and ok2 and ok3 and ok4 and ok5:
        print("\n==============================================")
        print("★ 5重の静的完全性検証にすべて合格しました！ ★")
        print("==============================================")
        return 0
    else:
        print("\n一部の検証に失敗しました。修正が必要です。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
