import fileinput
from collections import Counter

problem = [[int(value) for value in line.strip().split(' ')] for line in fileinput.input()]
n,k = problem.pop(0)
nums = Counter(problem.pop())
count = 0

for key in nums:
    lookup = k + key
    if k == 0 and lookup in nums:
        if lookup == key and nums[key] > 1:
            count += 1
        elif lookup != key:
            count += 1
    else:
        count += 1 if k + key in nums else 0
print(count)
