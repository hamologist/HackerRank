import fileinput
import os
from typing import Dict, Iterator


def sock_merchant(socks: Iterator[int]) -> int:
    pairs = 0
    lookup: Dict[int, int] = {}

    for sock in socks:
        current = lookup.get(sock, 0) + 1
        lookup[sock] = current

        if current % 2 == 0:
            pairs += 1

    return pairs


if __name__ == '__main__':
    output = open(os.getenv('OUTPUT_PATH'), 'w')
    stream: Iterator[str] = fileinput.input()

    next(stream)
    _socks = [int(sock) for sock in next(stream).split(' ')]

    output.write(str(sock_merchant(_socks)))
    output.close()
