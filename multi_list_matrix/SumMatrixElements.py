row, col = map(int, input().split(', '))

matrix = []

for r in range(row):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)

print(sum(map(sum, matrix)))
print(matrix)