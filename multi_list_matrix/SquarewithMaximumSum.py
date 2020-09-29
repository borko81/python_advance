rows, columns = map(int, input().split(', '))

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

print(matrix)