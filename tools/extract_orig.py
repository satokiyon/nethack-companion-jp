import sys

sys.stdout.reconfigure(encoding='utf-8')
start_line = int(sys.argv[1])
end_line = int(sys.argv[2])

with open('spoilers/companion.md', encoding='utf-8') as f:
    lines = f.readlines()

sub = lines[start_line-1:end_line]
print(''.join(sub))

