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
            price_dict[prices[x]].append(x+1)
        else:
            price_dict[prices[x]] = [x+1]

    for key in price_dict:
        lookup = dollars - key
        if lookup in price_dict:
            index_1 = price_dict[key].pop(0)
            index_2 = price_dict[lookup].pop(0)
            if index_1 > index_2:
                index_1, index_2 = index_2,index_1
            print('{0} {1}'.format(index_1, index_2))
            break
