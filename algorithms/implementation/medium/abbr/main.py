import fileinput
import os
from typing import Iterator


def abbreviation(a: str, b: str) -> bool:
    memo = {}

    def inner(a_pos: int, b_pos: int) -> bool:
        if a_pos == len(a) and b_pos == len(b):
            return True
        if b_pos == len(b):
            while a_pos < len(a):
                if a[a_pos].isupper():
                    return False
                a_pos += 1
            return True

        for pos in range(a_pos, len(a)):
            char = a[pos]
            if char == b[b_pos]:
                b_pos += 1
                if b_pos == len(b):
                    return inner(pos+1, b_pos)
            elif char.isupper():
                return False
            elif char.upper() == b[b_pos]:
                left = (pos+1, b_pos+1)
                right = (pos+1, b_pos)
                if left not in memo:
                    memo[left] = inner(pos+1, b_pos+1)
                if right not in memo:
                    memo[right] = inner(pos+1, b_pos)
                return memo[left] or memo[right]

        return b_pos == len(b)

    return inner(0, 0)


if __name__ == '__main__':
    _input: Iterator[str] = fileinput.input()
    _output = open(os.getenv('OUTPUT_PATH'), 'w')
    _ans = []
    next(_input)
    for _a in _input:
        _b = next(_input)
        _ans.append(abbreviation(_a.strip(), _b.strip()))
    _output.write('\n'.join(['YES' if resp else 'NO' for resp in _ans]))
