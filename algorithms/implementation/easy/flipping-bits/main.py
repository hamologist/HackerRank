import fileinput

BIT_FLIP = (2 ** 32) - 1

lines = [int(line.strip()) for line in fileinput.input()][1:]

for x in lines:
    print(x ^ BIT_FLIP)
