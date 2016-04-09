import fileinput

lines = [list(line.strip()) for line in fileinput.input()]
del lines[0]

for line in lines:
    palindrome = True
    for x in range(0, int(len(line)/2)):
        y = len(line)-x-1
        if line[x] != line[y]:
            del line[x]
            print(x if line == line[::-1] else y)
            palindrome = False
            break
    if palindrome: print(-1)
