import fileinput

lines = [[int(value) for value in line.strip().split(' ')] for line in fileinput.input()]
lines.pop(0)

for line in lines[1::2]:
    non_cont = max_cont = cont = 0
    largest_value = line[0]
    for value in line:
        non_cont += value if value > 0 else 0
        cont = max(cont + value, 0)
        max_cont = max(cont, max_cont)
        largest_value = max(value, largest_value)
    max_cont = largest_value if max_cont == 0 else max_cont
    non_cont = largest_value if non_cont == 0 else non_cont
    print(max_cont, non_cont)
