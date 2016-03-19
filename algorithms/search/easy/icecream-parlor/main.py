import fileinput

lines = list(fileinput.input())
test_cases = int(lines.pop(0))

for case in range(0, test_cases):
    finished = False
    pos = case * 3
    dollars = int(lines[pos])
    flavor_count = int(lines[pos+1])
    prices = [int(price) for price in lines[pos+2].split(' ')]
    price_dict = dict()

    for x in range(0, flavor_count):
        if prices[x] in price_dict:
            price_dict[prices[x]].append(x)
        else:
            price_dict[prices[x]] = [x]

    for key in price_dict:
        lookup = dollars - key
        if lookup in price_dict:
            print('{0} {1}'.format(key, lookup))
            break
