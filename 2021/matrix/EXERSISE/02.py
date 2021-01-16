r, c = map(int, input().split())

matrix = [[0] * c for _ in range(r)]
counter = 0

def check_for_equal(matrix, x, y, counter):
    a = matrix[x][y]
    b = matrix[x + 1][y]
    c = matrix[x + 1][y + 1]
    d = matrix[x][y + 1]
    if a == b == c == d:
        counter += 1
    return counter



for row in range(r):
    line = input().split()
    for col in range(c):
        matrix[row][col] = line[col]

for row in range(r - 1):
    for col in range(c - 1):
        counter = check_for_equal(matrix, row, col, counter)


print(counter)

