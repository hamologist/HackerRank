import fileinput
import re

def drill(grid, check):
    for j in range(0, len(grid)-len(check)+1):
        matches = [match.start() for match in re.finditer('(?={0})'.format(check[0]), grid[j])]
        for match in matches:
            splice = [ line[match:match+len(check[0])] for line in grid[j:j+len(check)] ]
            if drill_and_check(splice, check):
                return True
    return False

def drill_and_check(splice, check):
    match_count = 0
    for line in splice:
        if check[match_count] not in line:
            return False
        match_count += 1
    return True


lines = [line.strip() for line in fileinput.input()]
num_of_grids = int(lines.pop(0))
grids = []
checks = []

while(len(grids) < num_of_grids):
    r,c = [int(ele) for ele in lines.pop(0).split(' ')]
    grids.append(lines[:r])
    del lines[:r]
    r,c = [int(ele) for ele in lines.pop(0).split(' ')]
    checks.append(lines[:r])
    del lines[:r]

for i in range(0, len(grids)):
    if drill(grids[i], checks[i]):
        print("YES")
    else:
        print("NO")
