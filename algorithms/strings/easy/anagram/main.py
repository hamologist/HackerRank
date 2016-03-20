import fileinput

lines = [list(line.strip()) for line in fileinput.input()]
lines.pop(0)

for line in lines:
    not_in_count = 0
    large_count = 0
    if len(line) % 2 == 1:
        print(-1)
        continue
    left = dict()
    right = dict()
    for x in range(0, int(len(line)/2)):
        left_char = line[x]
        right_char = line[len(line)-x-1]
        left[left_char] = 1 if left_char not in left else left[left_char] + 1
        right[right_char] = 1 if right_char not in right else right[right_char] + 1

    for x in left:
        if x not in right:
            not_in_count += left[x]
        elif left[x] > right[x]:
            large_count += abs(left[x] - right[x])
    print(not_in_count + large_count)
