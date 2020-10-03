names = input().split(', ')

result = {i: [] for i in names}

hero_price = {i: [] for i in names}

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    name, item, price = command[0], command[1], command[2]
    price = int(price)

    if item in result[name]:
        continue
    else:
        result[name].append(item)
        hero_price[name].append(price)


for k, v in hero_price.items():
    print(f'{k} -> Items: {len(v)}, Cost: {sum(v)}')
