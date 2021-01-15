rows, cols = map(int, input().split(', '))

matrix = [[0] * cols for _ in range(rows)]
total_sum: int = 0

for r in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix[r] = line
    total_sum += sum(line)

print(total_sum)
print(matrix)