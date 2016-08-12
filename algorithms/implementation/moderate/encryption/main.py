import fileinput
import math

line = [x.strip() for x in fileinput.input()][0]
c = math.ceil(math.sqrt(len(line)))

print(' '.join([line[x::c] for x in range(c)]))
