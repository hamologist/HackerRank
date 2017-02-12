import fileinput

i, j, k = list(map(int, fileinput.input()[0].split(' ')))
count = 0

for x in range(i, j+1):
    if abs(x - int(str(x)[::-1])) % k == 0:
        count += 1

print(count)
