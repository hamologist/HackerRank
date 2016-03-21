import fileinput
from collections import Counter

lines = [list(line.strip()) for line in fileinput.input()]
lines.pop(0)

for line in lines:
    count = 0
    if len(line) % 2 == 1:
        print(-1)
        continue
    half_len = int(len(line)/2)
    left = Counter(line[:half_len])
    right = Counter(line[half_len:])

    for x in left:
        if x not in right:
            count += left[x]
        elif left[x] > right[x]:
            count += left[x] - right[x]
    print(count)
