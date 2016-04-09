import fileinput

lines = [ list(line.strip()) for line in fileinput.input() ]
T = int(''.join(lines.pop(0)))

for x in range(0,T*2,2):
    A,B = lines[x:x+2]
    answer = []
    while A and B:
        answer += A.pop(0) if A[0] < B[0] else B.pop(0)
    answer += A if A else B
    print(''.join(answer))
