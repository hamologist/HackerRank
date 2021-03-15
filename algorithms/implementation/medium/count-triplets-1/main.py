import fileinput
import os
from typing import Dict, Iterator, List


def count_triplets(nums: List[int], r: int) -> int:
    triplets = 0
    num_map: Dict[int, int] = {}
    r_map: Dict[int, int] = {}
    for num in reversed(nums):
        jump = r * num
        r_count = r_map.get(jump)
        if r_count:
            triplets += r_count

        num_count = num_map.get(jump)
        if num_count:
            r_map[num] = r_map.get(num, 0) + num_count

        num_map[num] = num_map.get(num, 0) + 1

    return triplets


if __name__ == '__main__':
    _user_input: Iterator[str] = fileinput.input()
    _, _r = [int(num) for num in next(_user_input).split(' ')]
    _nums = [int(num) for num in next(_user_input).split(' ')]

    output = open(os.getenv('OUTPUT_PATH'), 'w')
    output.write(str(count_triplets(_nums, _r)))
