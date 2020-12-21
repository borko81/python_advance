name_of_hero = input().split(', ')

result = {name: {'item': [], 'price': []} for name in name_of_hero}

while True:
    command = input()

    if command == 'End':
        break

    command = command.split('-')
    name, item, cost, *args = command
    cost = int(cost)

    if item not in result[name]['item']:
        result[name]['item'].append(item)
        result[name]['price'].append(cost)


for key, value in result.items():
    print(f"{key} -> Items: {len(value['item'])}, Cost: {sum(value['price'])}")


# 2
# names = input().split(', ')
#
# result = {i: [] for i in names}
#
# hero_price = {i: [] for i in names}
#
# while True:
#     command = input().split('-')
#     if command[0] == 'End':
#         break
#
#     name, item, price = command[0], command[1], command[2]
#     price = int(price)
#
#     if item in result[name]:
#         continue
#     else:
#         result[name].append(item)
#         hero_price[name].append(price)
#
#
# for k, v in hero_price.items():
#     print(f'{k} -> Items: {len(v)}, Cost: {sum(v)}')
