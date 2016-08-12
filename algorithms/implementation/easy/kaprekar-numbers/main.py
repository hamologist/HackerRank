import fileinput

def isKaprekar(x):
    y = str(x * x)
    s = int(len(y)/2)
    l,r = y[:s] or 0, y[s:]
    return (True if int(l) + int(r) == x else False)

p,q = [int(num.strip()) for num in fileinput.input()]

ans = ' '.join([str(x) for x in range(p, q+1) if isKaprekar(x)])
print(ans if ans is not '' else 'INVALID RANGE')
