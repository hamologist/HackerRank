import fileinput

class stack:
    def __init__(self, nums):
        self.height = sum(nums)
        self.nums = nums

lines = [[int(num) for num in line.strip().split()] for line in fileinput.input()][1:]
stacks = [stack(line) for line in lines]

while (stacks[0].height != stacks[1].height or stacks[0].height != stacks[2].height):
    x = stacks[0]
    if stacks[1].height > x.height:
        x = stacks[1]
    elif stacks[2].height > x.height:
        x = stacks[2]
    x.height -= x.nums[0]
    x.nums.pop(0)

print(stacks[0].height)
