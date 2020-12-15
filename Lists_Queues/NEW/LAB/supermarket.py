from collections import deque

result = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(result)} people remaining.')
        break

    elif command == 'Paid':
        while result:
            print(result.popleft())

    else:
        result.append(command)
