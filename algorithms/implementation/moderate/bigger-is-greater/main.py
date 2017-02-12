import fileinput
from collections import defaultdict


def gen_index(line):
    index = defaultdict(list)
    for pos in range(0, len(line)):
        index[line[pos]].append(pos)

    return index


def minimal_reorder(line):
    l = len(line)
    index = gen_index(line)
    move = None
    for pos in range(l-1, -1, -1):
        c = line[pos]
        for key, value in index.items():
            if c < key:
                for v in value:
                    if v > pos and (move is None or key < line[move]):
                        move = v
        if move is not None:
            line = list(line)
            a = line[pos]
            b = line[move]
            line[pos] = b
            line[move] = a
            return ''.join(line[:pos+1] + sorted(line[pos+1:]))
    return line


def run():
    user_input = [line for line in fileinput.input()]
    t = int(user_input[0])
    lines = [line.strip() for line in user_input[1:]]

    for line in lines:
        reorder = minimal_reorder(line)
        if reorder != line:
            print(reorder)
        else:
            print('no answer')

if __name__ == '__main__':
    run()
