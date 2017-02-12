import fileinput

nums = sorted([int(num) for num in fileinput.input()[0].strip().split(' ')])

print("{0} {1}".format(sum(nums[0:4]), sum(nums[1:5])))
