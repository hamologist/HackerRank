import fileinput
from typing import List


def breaking_records(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0

    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1

    print("{} {}".format(max_count, min_count))


if __name__ == '__main__':
    lines: List[str] = [line.strip() for line in fileinput.input()]
    breaking_records([int(x) for x in lines[1].split(' ')])
