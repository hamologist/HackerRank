import fileinput

lines = [list(line.strip()) for line in fileinput.input()][1:]
print(len(set.intersection(*map(lambda x: set(x), lines))))
