import fileinput

lines = [line.strip() for line in fileinput.input()]
N, M = [int(num) for num in lines.pop(0).split(' ')]
current_max = 0
max_known = 0
lines = [int(line, 2) for line in lines]

for y in range(0, N):
    for x in range(y+1, N):
        topics = "{0:b}".format(lines[y] | lines[x]).count('1')
        if topics > current_max:
            current_max = topics
            max_known = 1
        elif topics == current_max:
            max_known += 1

print(current_max)
print(max_known)
