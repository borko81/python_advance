n = int(input())
matrix = [
    [int(x) for x in input().split(' ')] for _ in range(n)
]

coorindate = input().split()
coordinates = []
for p in coorindate:
    coordinates.append(p.split(','))


def is_valid_ccorinate(matrix, position_one, position_two):
    return 0 <= position_one < n and 0 <= position_two < n


def boom(matrix, position_one, position_two):
    if is_valid_ccorinate(matrix, position_one - 1, position_two) \
    and matrix[position_one - 1][position_two] > 0:
        matrix[position_one - 1][position_two] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one + 1, position_two) \
    and matrix[position_one + 1][position_two] > 0:
        matrix[position_one + 1][position_two] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one, position_two + 1) \
    and matrix[position_one][position_two + 1] > 0:
        matrix[position_one][position_two + 1] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one, position_two - 1) \
    and matrix[position_one][position_two - 1] > 0:
        matrix[position_one][position_two - 1] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one + 1, position_two - 1) \
    and matrix[position_one + 1][position_two - 1] > 0:
        matrix[position_one + 1][position_two - 1] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one + 1, position_two + 1) \
    and matrix[position_one + 1][position_two + 1] > 0:
        matrix[position_one + 1][position_two + 1] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one - 1, position_two - 1) \
    and matrix[position_one - 1][position_two - 1] > 0:
        matrix[position_one - 1][position_two - 1] -= matrix[position_one][position_two]
    if is_valid_ccorinate(matrix, position_one - 1, position_two + 1) \
    and matrix[position_one - 1][position_two + 1] > 0:
        matrix[position_one - 1][position_two + 1] -= matrix[position_one][position_two]
    matrix[position_one][position_two] = 0


for i in coordinates:
    x, c, *args = map(int, i[:])
    if matrix[x][c] > 0:
        boom(matrix, x, c)

sumata = 0
not_dead = 0
for row in matrix:
    for c in row:
        if c > 0:
            not_dead += 1
            sumata += c


print(f"Alive cells: {not_dead}")
print(f"Sum: {sumata}")
for row in matrix:
    print(" ".join(str(x) for x in row))
