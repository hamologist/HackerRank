import fileinput
import os
from typing import Dict, Iterator


def sherlock_and_anagrams(query: str) -> int:
    query_map: Dict[str, int] = {}
    anagrams = 0

    for window in range(1, len(query)):
        for pos in range(0, len(query) - window + 1):
            substring = ''.join(sorted(query[pos:pos+window]))
            current_count = query_map.get(substring, 0) + 1
            query_map[substring] = current_count

            if current_count > 1:
                anagrams += current_count - 1

    return anagrams


if __name__ == '__main__':
    _userInput: Iterator[str] = fileinput.input()
    _output = open(os.getenv("OUTPUT_PATH"), 'w')
    next(_userInput)

    _output.write("\n".join((str(sherlock_and_anagrams(solution.strip())) for solution in _userInput)))
    _output.close()
