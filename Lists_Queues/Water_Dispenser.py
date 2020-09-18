from collections import deque

quantity_of_water = int(input())

person = deque()

while True:
    command = input()
    if command == 'Start':
        break
    person.append(command)

while person:
    command = input()

    if command.startswith('refill'):
        ref = command.split()[1]
        quantity_of_water += int(ref)
        continue

    per = person.popleft()

    if int(command) <= quantity_of_water:
        quantity_of_water -= int(command)
        print(f'{per} got water')
    else:
        print(f'{per} must wait')

print(f'{quantity_of_water} liters left')
