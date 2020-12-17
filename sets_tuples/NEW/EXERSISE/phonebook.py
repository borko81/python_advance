phones = {}

while True:
    line = input()
    if '-' in line:
        name, phone = line.split('-')
        phones[name] = phone
    else:
        num_of_row = int(line)
        break


for _ in range(num_of_row):
    name = input()
    if name in phones:
        print(f"{name} -> {phones[name]}")
    else:
        print(f"Contact {name} does not exist.")

