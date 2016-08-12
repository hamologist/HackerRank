import fileinput

l,r = [int(line.strip()) for line in fileinput.input()]
ans = 0

for y in range(l, r+1):
    for x in range(y, r+1):
        xor = y ^ x
        ans = xor if ans < xor else ans

print(ans)
