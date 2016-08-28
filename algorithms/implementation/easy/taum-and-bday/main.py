import fileinput

lines = [[int(num) for num in line.strip().split(' ')] for line in fileinput.input()]
T = lines.pop(0)[0]

for i in range(0, T):
    B, W = lines[i*2]
    X, Y, Z = lines[i*2+1]
    X = X if Y + Z > X else Y + Z
    Y = Y if X + Z > Y else X + Z
    print((X * B) + (Y * W))
