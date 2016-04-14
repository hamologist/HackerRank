import fileinput

lines = [ list(line.strip()) for line in fileinput.input() ]
n = int(''.join(lines.pop(0)))

for y in range(1, n-1):
    for x in range(1, n-1):
        cur = int(lines[y][x])
        border = list(lines[y-1][x] + lines[y][x-1] + lines[y][x+1] + lines[y+1][x])
        if 'X' not in border and all(int(i) < cur for i in border):
            lines[y][x] = 'X'
for line in lines:
    print(''.join(line))
