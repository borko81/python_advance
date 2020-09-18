storage = []

while True:
    name = input()
    if name == 'End':
        print(f'{len(storage)} people remaining.')
        break

    elif name == 'Paid':
        while storage:
            print(storage.pop())

    else:
        storage.insert(0, name)
