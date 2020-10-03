name = input().split(', ')
row = int(input())

foods = {n: [] for n in name}
quality = {n: 0 for n in name}
quantity = {n: 0 for n in name}


for _ in range(row):
    temp = input().split(' - ')
    category = temp[0]
    item_name = temp[1]
    rest = temp[2].split(';')
    quant = int(rest[0].split(':')[-1])
    qual = int(rest[1].split(':')[-1])

    foods[category].append(item_name)
    quality[category] += qual
    quantity[category] += quant


print(f'Count of items: {sum([quantity[i] for i in quantity])}')
print(f'Average quality: {(sum([quality[i] for i in quality]) / len(foods)):.2f}')

for k, v in foods.items():
    print(f"{k} -> {', '.join(n for n in v)}")
