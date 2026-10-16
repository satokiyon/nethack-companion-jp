#!/usr/bin/env python3
"""
docs/segments_jp/step_XXX.md を順次結合し、spoilers/companion.jp.md を生成するスクリプト。
あわせて原著 spoilers/companion.md の見出しから Pandoc 準拠の英語アンカーID ({#xxxxx}) を算出し、
各セグメントの見出しに未付与の場合は自動補完・同期する。
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


def extract_en_headings(lines):
    """コードブロックを除いた見出し行 (hashes, text) のリストを返す。"""
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


def apply_anchor_to_jp_heading(line, en_slug):
    """日本語見出し行に英語アンカー {#en_slug} を付与または統合する。"""
    m_attr = re.match(r'^(.+?)\s+\{([#\.][^}`]*)\}\s*$', line)
    if m_attr:
        prefix = m_attr.group(1)
        attr_content = m_attr.group(2).strip()
        if re.search(r'(?:^|\s)#([^\s}]+)', attr_content):
            attr_content = re.sub(r'(^|\s)#([^\s}]+)', f'\\1#{en_slug}', attr_content, count=1)
        else:
            attr_content = f"#{en_slug} {attr_content}"
        return f"{prefix} {{{attr_content}}}"
    else:
        return f"{line.rstrip()} {{#{en_slug}}}"


def sync_segment_headings(jp_text, en_slugs):
    """セグメント内の見出しに英語アンカーIDを適用する。"""
    lines = jp_text.splitlines()
    out_lines = []
    in_code = False
    h_idx = 0
    updated_count = 0

    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
        if not in_code and re.match(r'^#{1,6}\s+.+$', line):
            if h_idx < len(en_slugs):
                new_line = apply_anchor_to_jp_heading(line, en_slugs[h_idx])
                if new_line != line:
                    updated_count += 1
                line = new_line
            h_idx += 1
        out_lines.append(line)

    return "\n".join(out_lines), updated_count


def assemble(
    progress_json='docs/translation_progress.json',
    segments_dir='docs/segments_jp',
    orig_md='spoilers/companion.md',
    output_md='spoilers/companion.jp.md'
):
    with open(progress_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    en_lines = []
    if os.path.exists(orig_md):
        with open(orig_md, 'r', encoding='utf-8') as f:
            en_lines = f.read().splitlines()

    os.makedirs(os.path.dirname(output_md), exist_ok=True)

    parts = []
    missing = []
    total = len(data['segments'])
    seen_counts = {}
    total_anchors_synced = 0
    modified_segments = 0

    for s in data['segments']:
        seg_id = s['id']
        seg_file = os.path.join(segments_dir, f"{seg_id}.md")

        # 原著の該当行範囲から見出しスラッグを算出
        en_slugs = []
        if en_lines:
            seg_en_lines = en_lines[s['start_line'] - 1 : s['end_line']]
            for _, h_text in extract_en_headings(seg_en_lines):
                en_slugs.append(pandoc_slug(h_text, seen_counts))

        if os.path.exists(seg_file):
            with open(seg_file, 'r', encoding='utf-8') as sf:
                raw_content = sf.read().rstrip()

            if en_slugs:
                synced_content, updated = sync_segment_headings(raw_content, en_slugs)
                if updated > 0:
                    with open(seg_file, 'w', encoding='utf-8') as wf:
                        wf.write(synced_content + "\n")
                    total_anchors_synced += updated
                    modified_segments += 1
                raw_content = synced_content

            parts.append(raw_content)
        else:
            missing.append(seg_id)

    combined_text = "\n\n".join(parts) + "\n"

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(combined_text)

    assembled_count = len(parts)
    if total_anchors_synced > 0:
        print(f"英語アンカー同期: {modified_segments} セグメント内の {total_anchors_synced} 個の見出しに英語アンカーIDを付与・同期しました。")
    print(f"アセンブル完了: {assembled_count}/{total} セグメントを {output_md} に出力しました。")
    if missing:
        print(f"未アセンブルのセグメント: {len(missing)} 件 (先頭: {missing[0]})")


if __name__ == '__main__':
    assemble()
