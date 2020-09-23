result = {}

name_with_phone = input()

while not name_with_phone.isdigit():
    name, phone = name_with_phone.split('-')
    result[name] = phone
    name_with_phone = input()


num = int(name_with_phone)
for _ in range(num):
    name_to_search = input()
    if name_to_search in result:
        print(f'{name_to_search} -> {result[name_to_search]}')
    else:
        print(f'Contact {name_to_search} does not exist.')