phonebook = {}
number_of_names = None

while True:
    line = input()
    if line.isdigit():
        number_of_names = int(line)
        break

    name, phone = line.split('-')
    phonebook[name] = phone

for _ in range(number_of_names):
    line = input()
    if line in phonebook:
        print(f"{line} -> {phonebook[line]}")
    else:
        print(f"Contact {line} does not exists.")

