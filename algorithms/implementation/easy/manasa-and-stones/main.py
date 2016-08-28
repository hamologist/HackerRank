import fileinput

lines = [ int(line.strip()) for line in fileinput.input() ]
T = lines.pop(0)

for t in range(0, T):
    n = lines[3 * t]
    a = lines[3 * t + 1]
    b = lines[3 * t + 2]
    ans = set()
    for c in range(0, n):
        ans.add( (a*c) + (b*((n-1)-c)) )
    print(' '.join(str(x) for x in sorted(ans)))
