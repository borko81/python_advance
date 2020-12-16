n = int(input())

result = []

for _ in range(n):
    line = input()
    command, number = line.split(', ')
    if command == 'IN':
        result.append(number)
    else:
        result.pop(result.index(number))

if len(result):
    [print(x) for x in result]
else:
    print("Parking Lot is Empty")