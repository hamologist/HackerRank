import fileinput, datetime

lines = [ [ int(n) for n in line.strip().split(' ') ] for line in fileinput.input() ]

returned = datetime.date(lines[0][2], lines[0][1], lines[0][0])
expected = datetime.date(lines[1][2], lines[1][1], lines[1][0])
delta = returned - expected

if returned.year > expected.year:
    print(10000)
elif returned.year < expected.year:
    print(0)
elif returned.month > expected.month:
    print(500 * (returned.month - expected.month))
else:
    print(15 * delta.days if delta.days > 0 else 0)
