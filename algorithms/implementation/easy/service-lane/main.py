import fileinput

lines = [[int(ele) for ele in line.strip().split(' ')] for line in fileinput.input()][1:]
lane = lines.pop(0)

for line in lines:
    print(min(lane[line[0]:line[1]+1]))
