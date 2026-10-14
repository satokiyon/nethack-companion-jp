import json
import sys

with open('docs/translation_progress.json', encoding='utf-8') as f:
    data = json.load(f)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 72
count = int(sys.argv[2]) if len(sys.argv) > 2 else 15

for s in data['segments'][start:start+count]:
    print(f"{s['id']}: L{s['start_line']}-L{s['end_line']} {s['orig_header']} ({s['title']}) [{s['status']}]")

