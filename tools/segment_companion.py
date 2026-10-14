#!/usr/bin/env python3
"""
companion.md を H4（およびH4がない区間はH3/H2）を基準とした約50〜100行単位の安全なセグメントに分割し、
docs/translation_progress.json を初期化・更新するスクリプト。
"""

import json
import os
import re

def create_segments(md_path='spoilers/companion.md', output_json='docs/translation_progress.json'):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    
    # 見出し位置を検出 (H1 - H4)
    headers = []
    current_part = "Intro"
    current_h3 = "Overview"

    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 2:
                current_part = title
            elif level == 3:
                current_h3 = title
            headers.append({
                'line_num': line_num,
                'level': level,
                'title': title,
                'part': current_part,
                'h3': current_h3
            })

    # 見出しの境界に基づいてセグメントを作成
    # 長すぎるセグメント（> 150行）は空白行等でさらに分割する
    segments = []
    
    for i in range(len(headers)):
        cur = headers[i]
        start_line = cur['line_num']
        end_line = headers[i + 1]['line_num'] - 1 if i + 1 < len(headers) else total_lines
        
        # 1行目〜最初の見出し前までをカバー
        if i == 0 and start_line > 1:
            segments.append({
                'id': f"step_{len(segments)+1:03d}",
                'part': "Intro",
                'section': "Header",
                'title': "Title and Preamble",
                'start_line': 1,
                'end_line': start_line - 1,
                'line_count': start_line - 1,
                'status': "pending",
                'notes': ""
            })
            
        seg_lines = end_line - start_line + 1
        
        # もし1つのセクションが180行以上ある場合、段落（空行）を基準に約80〜120行で分割する
        if seg_lines > 180:
            sub_start = start_line
            chunk_target = 100
            cur_line = sub_start
            while cur_line <= end_line:
                cand_end = min(cur_line + chunk_target, end_line)
                if cand_end < end_line:
                    # 空行を探す
                    split_line = cand_end
                    for scan in range(cand_end, max(cur_line + 40, cand_end - 40), -1):
                        if lines[scan - 1].strip() == "":
                            split_line = scan
                            break
                    seg_sub_end = split_line
                else:
                    seg_sub_end = end_line
                
                part_idx = len(segments) + 1
                segments.append({
                    'id': f"step_{part_idx:03d}",
                    'part': cur['part'],
                    'section': cur['h3'],
                    'title': f"{cur['title']} (Part {len([s for s in segments if s.get('orig_header') == cur['title']]) + 1})",
                    'orig_header': cur['title'],
                    'start_line': cur_line,
                    'end_line': seg_sub_end,
                    'line_count': seg_sub_end - cur_line + 1,
                    'status': "pending",
                    'notes': ""
                })
                cur_line = seg_sub_end + 1
        else:
            part_idx = len(segments) + 1
            segments.append({
                'id': f"step_{part_idx:03d}",
                'part': cur['part'],
                'section': cur['h3'],
                'title': cur['title'],
                'orig_header': cur['title'],
                'start_line': start_line,
                'end_line': end_line,
                'line_count': seg_lines,
                'status': "pending",
                'notes': ""
            })

    # 既存の progress.json があればステータスを維持
    existing_status = {}
    if os.path.exists(output_json):
        try:
            with open(output_json, 'r', encoding='utf-8') as f:
                old_data = json.load(f)
                for item in old_data.get('segments', []):
                    existing_status[item['id']] = (item['status'], item.get('notes', ''))
        except Exception:
            pass

    for s in segments:
        if s['id'] in existing_status:
            s['status'] = existing_status[s['id']][0]
            s['notes'] = existing_status[s['id']][1]

    manifest = {
        'total_segments': len(segments),
        'total_lines': total_lines,
        'completed_segments': len([s for s in segments if s['status'] in ('reviewed', 'integrated')]),
        'segments': segments
    }

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Total segments created: {len(segments)}")
    print(f"Saved manifest to {output_json}")

if __name__ == '__main__':
    create_segments()

