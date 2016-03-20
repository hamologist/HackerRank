import fileinput

a,b,n = [int(x) for x in fileinput.input()[0].strip().split(' ')]

for x in range(2, n):
    new_a = b
    b = b**2 + a
    a = new_a
print(b)
