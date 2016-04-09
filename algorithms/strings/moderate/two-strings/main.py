import fileinput

lines = [ line.strip() for line in fileinput.input() ]
T = int(lines.pop(0))

for x in range(0,T*2,2):
    a = set(lines[x])
    b = set(lines[x+1])
    print('YES') if len(set.intersection(a,b)) else print('NO')
