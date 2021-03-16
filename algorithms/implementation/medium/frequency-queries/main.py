import fileinput
import os
from typing import Dict, Iterator, List


def freq_query(queries: List[List[int]]) -> List[int]:
    output = []
    freq_map: Dict[int, int] = {}
    num_map: Dict[int, int] = {}

    for query in queries:
        op = query[0]
        num = query[1]

        if op == 1:
            current_freq = num_map.get(num, 0) + 1
            num_map[num] = current_freq
            freq_map[current_freq] = freq_map.get(current_freq, 0) + 1

            if current_freq > 1:
                freq_map[current_freq - 1] = freq_map.get(current_freq - 1) - 1
        elif op == 2:
            current_freq = num_map.get(num, 0) - 1

            if current_freq > 0:
                freq_map[current_freq] = freq_map.get(current_freq, 0) + 1
            if current_freq >= 0:
                num_map[num] = current_freq
                freq_map[current_freq + 1] = freq_map.get(current_freq + 1) - 1
        elif freq_map.get(num):
            output.append(1)
        else:
            output.append(0)

    return output


if __name__ == '__main__':
    _user_input: Iterator[str] = fileinput.input()
    next(_user_input)
    _queries = [[int(num) for num in query.strip().split()] for query in _user_input]

    _output = open(os.getenv('OUTPUT_PATH'), 'w')
    _output.write("\n".join((str(num) for num in freq_query(_queries))))
