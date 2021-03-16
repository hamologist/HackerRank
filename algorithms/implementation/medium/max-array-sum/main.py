import fileinput
import os
from typing import Iterator, List


def max_subset_sum(nums: List[int]) -> int:
    last = nums[0]
    before = max(nums[1], last)

    for num in nums[2:]:
        current_max = max(num, before, last + num)
        last = before
        before = current_max
    return before


if __name__ == '__main__':
    _input: Iterator[str] = fileinput.input()
    next(_input)
    _nums = [int(num) for num in next(_input).split(' ')]

    _output = open(os.getenv('OUTPUT_PATH'), 'w')
    _output.write(str(max_subset_sum(_nums)))