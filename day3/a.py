tree = 0
lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(str(line).rstrip())
    f.close()
pos = 0
for line in lines:
    if line[pos] == '#':
        tree += 1
        print(pos)
    pos += 3
    if pos >= len(line):
        pos = pos - len(line)
    
print(tree)