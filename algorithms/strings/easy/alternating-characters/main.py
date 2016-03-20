import fileinput
import re

lines = [line.strip() for line in fileinput.input()]
lines.pop(0)

for line in lines:
    matches = [len(match) - 1 for match in re.findall(r'AA+|BB+', line) if len(match)]
    print(sum(matches))
