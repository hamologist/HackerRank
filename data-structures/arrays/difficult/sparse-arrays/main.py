import fileinput
from collections import Counter

lines = [ line.strip() for line in fileinput.input() ]
N = int(lines.pop(0))
words = Counter()
for word in lines[0:N]:
    words[word] += 1
for line in lines[N+1:]:
    print(words[line]) if line in words else print(0)
