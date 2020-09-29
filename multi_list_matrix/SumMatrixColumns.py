row, col = map(int, input().split(', '))

matrix = []

for r in range(row):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)


for result in [sum(i) for i in zip(*matrix)]:
    print(result)