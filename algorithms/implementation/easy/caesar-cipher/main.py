import fileinput

lines = [ line.strip() for line in fileinput.input() ]
N = int(lines.pop(0))
S = [ ord(c) for c in lines.pop(0) ]
K = int(lines.pop(0))

print(''.join([ 
    chr((o-65+K)%26+65) if o > 64 and o < 91 else 
    chr((o-97+K)%26+97) if o > 96 and o < 123 else 
    chr(o) for o in S
    ])
)
