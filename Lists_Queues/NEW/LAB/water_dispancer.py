from collections import deque

peoples = deque()

quantity = int(input())

while True:
    people = input()
    if people == 'Start':
        break

    peoples.append(people)


while True:
    command = input()
    if command == 'End':
        print(f"{quantity} liters left")
        break

    elif command.startswith('refill'):
        _, quant, *args = command.split()
        quant = int(quant)
        quantity += quant

    else:
        command = int(command)
        temp = peoples.popleft()
        if command <= quantity:
            print(f"{temp} got water")
            quantity -= command
        else:
            print(f"{temp} must wait")
