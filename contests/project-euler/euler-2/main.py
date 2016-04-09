import fileinput

lines = [ int(line.strip()) for line in fileinput.input() ][1:]

for line in lines:
    prev = 1
    current = 2
    answer = 0
    while current <= line:
        answer += current if current % 2 == 0 else 0
        temp = current
        current += prev
        prev = temp
    print(answer)
