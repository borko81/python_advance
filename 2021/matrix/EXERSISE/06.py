n = int(input())
matrix = []
result = 0

for r in range(n):
    matrix.append(list(input()))

possible = (
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
)


def is_valid(size, x, y, p):
    return 0 <= x + p[0] < n and 0 <= y + p[1] < n


def killed_knight(matrix, x, y):
    x = int(x)
    y = int(y)
    kill = 0
    for p in possible:
        if is_valid(n, x, y, p) and matrix[x + p[0]][y + p[1]] == 'K':
            kill += 1
    return kill


while True:
    max_kill = 0
    position = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'K':
                temp = killed_knight(matrix, r, c)
                if temp > max_kill:
                    max_kill = temp
                    position = [r, c]
    if max_kill == 0:
        break

    matrix[position[0]][position[1]] = '0'
    result += 1


print(result)
