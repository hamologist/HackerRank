import sys

nums = [ int(x) for x in sys.stdin.readlines()[1].split(' ') ]
print(sum(nums))
