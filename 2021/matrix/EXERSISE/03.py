row, col = map(int, input().split())
matrix = [[0] * col for _ in range(row)]


possible = (
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2)
)

max_result = -999
position = []
x = 0
y = 0


def check_for_max(matrix, row, col, possible):
    temp = 0
    for p in possible:
        temp += matrix[row + p[0]][col + p[1]]
    return temp


for r in range(row):
    line = [int(x) for x in input().split()]
    for c in range(col):
        matrix[r][c] = line[c]


for r in range(row - 2):
    for c in range(col - 2):
        score = check_for_max(matrix, r, c, possible)
        if score > max_result:
            max_result = score
            position = []
            position.append([matrix[r + p[0]][c + p[1]] for p in possible[0:3]])
            position.append([matrix[r + p[0]][c + p[1]] for p in possible[3:6]])
            position.append([matrix[r + p[0]][c + p[1]] for p in possible[6:9]])


print(f"Sum = {max_result}")
for i in position:
    print(" ".join(str(x) for x in i))
