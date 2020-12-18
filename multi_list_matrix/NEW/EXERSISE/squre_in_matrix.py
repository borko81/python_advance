a, b = map(int, input().split())

matrix = [[x for x in input().split()] for _ in range(a)]

count = 0


def check(matrix, x, y):
    return matrix[x][y] == matrix[x + 1][y] == matrix[x][y + 1] == matrix[x + 1][y + 1]


for x in range(a - 1):
    for y in range(b - 1):
        if check(matrix, x, y):
            count += 1

print(count)