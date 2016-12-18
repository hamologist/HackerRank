import fileinput

A,B = [list(map(int, line.strip().split(' '))) for line in fileinput.input()]
Ac = Bc = 0

for i in range(0, len(A)):
    if A[i] > B[i]:
        Ac += 1
    elif A[i] != B[i]:
        Bc += 1

print("{0} {1}".format(Ac, Bc))
