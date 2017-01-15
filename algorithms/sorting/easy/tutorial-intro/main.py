import fileinput
from math import ceil

def binary_search(v, a):
    i = ceil(len(a) / 2) - 1
    cut = i + 1
    while a[i] != v:
        cut = ceil(cut / 2)
        if a[i] > v:
            i -= cut
        else:
            i += cut

    return i


lines = [
    list(
        map(int, line.strip().split(' '))
    ) for line in fileinput.input()
]
V, n, ar = lines[0].pop(), lines[1].pop(), lines[2]

print(binary_search(V, ar))
