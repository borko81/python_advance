categories = input().split(', ')

result = {categorie: {'item_name': [], 'item_quntity': [], 'item_quality': []} for categorie in categories}

row = int(input())

for _ in range(row):
    line = input().split(' - ')

    categorie, item_name = line[:2]
    temp = line[2].split(';')

    item_quantity = int(temp[0].split(':')[1])
    item_quality = int(temp[1].split(':')[-1])

    result[categorie]['item_name'].append(item_name)
    result[categorie]['item_quntity'].append(item_quantity)
    result[categorie]['item_quality'].append(item_quality)

item_quantity_sum = 0
item_quality_sum = 0

for key, val in result.items():
    item_quantity_sum += sum(val['item_quntity'])
    item_quality_sum += sum(val['item_quality'])


print(f"Count of items: {item_quantity_sum}")
print(f"Average quality: {(item_quality_sum / len(categories)):.2f}")

for key, val in result.items():
    print(f"{key} -> {', '.join(val['item_name'])}")


