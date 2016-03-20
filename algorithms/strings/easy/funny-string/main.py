import fileinput

lines = [line.strip() for line in fileinput.input()]
lines.pop(0)

for line in [list(line) for line in lines]:
    line = [ord(char) for char in line]
    rev_line = line[::-1]
    funny = True
    for x in range(1, len(line)-1):
        if abs(line[x] - line[x+1]) != abs(rev_line[x] - rev_line[x+1]):
            funny = False
            break
    if funny:
        print('Funny')
    else:
        print('Not Funny')
