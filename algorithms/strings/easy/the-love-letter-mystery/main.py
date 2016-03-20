import fileinput

lines = [list(line.strip()) for line in fileinput.input()]
lines.pop(0)

for line in lines:
    count = 0
    for x in range(0, int(len(line)/2)):
        left, right = ord(line[x]), ord(line[len(line)-x-1])
        while left > right:
            count += 1
            left -= 1
        while right > left:
            count += 1
            right -= 1
    print(count)
