import fileinput

finput = fileinput.input()
s, t = list(map(int, finput[0].split(' ')))
a, b = list(map(int, finput[1].split(' ')))
m, n = list(map(int, finput[2].split(' ')))
apples = list(map(int, finput[3].split(' ')))
oranges = list(map(int, finput[4].split(' ')))
apple_count = orange_count = 0

for apple in apples:
    landing = a + apple
    if landing >= s and landing <= t:
        apple_count += 1
        
for orange in oranges:
    landing = b + orange
    if landing >= s and landing <= t:
        orange_count += 1

print(apple_count)
print(orange_count)
