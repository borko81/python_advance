a, b = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(a)]


def check(matrix, x, y):
    result =    matrix[x][y] +\
                matrix[x][y+1] +\
                matrix[x][y+2] + \
                matrix[x + 1][y] + \
                matrix[x + 1][y+1]+\
                matrix[x + 1][y+2]+\
                matrix[x + 2][y] + \
                matrix[x + 2][y + 1] +\
                matrix[x + 2][y + 2]
    return result, [
        [
            matrix[x][y],
            matrix[x][y+1],
            matrix[x][y+2]
        ],
        [
            matrix[x + 1][y],
            matrix[x + 1][y+1],
            matrix[x + 1][y+2],
        ],
        [
            matrix[x + 2][y],
            matrix[x + 2][y + 1],
            matrix[x + 2][y + 2],
        ]
    ]

count = -9
posiiton = []

for x in range(a - 2):
    for y in range(b - 2):
        temp = check(matrix, x, y)
        if temp[0] > count:
            count = temp[0]
            posiiton = temp[1]

print(f"Sum = {count}")
for i in posiiton:
    print(f"{' '.join(str(x) for x in i)}")


# -------------2----------------------
row, col = [int(x) for x in input().split()]
matrix = []

for r in range(row):
    matrix.append([int(x) for x in input().split()])

sum_max = -999999
point = []

for r in range(row - 2):
    for c in range(col - 2):
        p = []
        pos = 0
        s = 0
        for rr in range(r, r + 3):
            p.append([])
            for cc in range(c, c + 3):
                p[pos].append(matrix[rr][cc])
                s += matrix[rr][cc]
            pos += 1
        if s > sum_max:
            sum_max = s
            point = p
        s = 0

print(f'Sum = {sum_max}')
for _ in point:
    print(' '.join([str(x) for x in _]))