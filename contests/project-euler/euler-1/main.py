import fileinput
import itertools

lines = [ int(line.strip()) for line in fileinput.input() ][1:]

for num in lines:
    x = int((num-1) / 3)
    threes = 3 * int((x * (x+1)) >> 1)
    y = int((num-1) / 5)
    fives = 5 * int((y * (y+1)) >> 1)
    z = int((num-1) / 15)
    fifteens = 15 * int((z * (z+1)) >> 1)
    print(threes + fives - fifteens)
