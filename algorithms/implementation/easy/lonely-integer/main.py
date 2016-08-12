import fileinput

lines = [map(int, line.strip().split(' ')) for line in fileinput.input()]
N, A = lines
ans = 0

for x in A:
    ans ^= x

print(ans)
