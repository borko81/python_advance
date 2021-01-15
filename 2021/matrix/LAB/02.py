rows, cols = map(int, input().split(', '))

matrix = [[0] * cols for _ in range(rows)]

for r in range(rows):
    line = [int(x) for x in input().split(' ')]
    matrix[r] = line


for i in zip(*matrix):
    print(sum(i))