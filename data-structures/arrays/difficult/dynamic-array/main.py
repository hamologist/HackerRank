import fileinput

lines = [[int(ele) for ele in line.strip().split(' ')] for line in fileinput.input()]

N, Q = lines.pop(0)
lastans = 0
seq = [ [] for x in range(0, N) ]

for line in lines:
    if line[0] == 1:
        seq[(line[1]^lastans)%N].append(line[2])
    else:
        lastans = seq[(line[1]^lastans)%N][line[2]%len(seq[(line[1]^lastans)%N])]
        print(lastans)
