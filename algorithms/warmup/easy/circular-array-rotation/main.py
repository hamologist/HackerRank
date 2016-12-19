import fileinput

lines = [list(map(int, line.strip().split(' '))) for line in fileinput.input()]
n,k,q = lines.pop(0)
N = lines.pop(0)
lines = list(map(lambda x: x[0], lines))

for m in lines:
    print(N[(m-k)%n])
