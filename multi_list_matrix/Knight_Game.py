size = int(input())
matrix = []
result = 0

for _ in range(size):
    matrix.append(list(input()))


def is_valid(row, pos, size):
    if 0 <= row < size and 0 <= pos < size:
        return True


def get_killed(r, c, size, matrix):
    killed_knights = 0
    if is_valid(r + 2, c + 1, size) and matrix[r + 2][c + 1] == 'K':
            killed_knights += 1
    if is_valid(r + 2, c - 1, size) and matrix[r + 2][c - 1] == 'K':
            killed_knights += 1
    if is_valid(r - 2, c + 1, size) and matrix[r - 2][c + 1] == 'K':
            killed_knights += 1
    if is_valid(r - 2, c - 1, size) and matrix[r - 2][c - 1] == 'K':
            killed_knights += 1
    if is_valid(c - 2, r - 1, size) and matrix[r - 1][c - 2] == 'K':
            killed_knights += 1
    if is_valid(c - 2, r + 1, size) and matrix[r + 1][c - 2] == 'K':
            killed_knights += 1
    if is_valid(c + 2, r - 1, size) and matrix[r - 1][c + 2] == 'K':
            killed_knights += 1
    if is_valid(c + 2, r + 1, size) and matrix[r + 1][c + 2] == 'K':
            killed_knights += 1
    return killed_knights


while True:
    boss_killer = 0
    boss_position = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                killed = get_killed(row, col, size, matrix)
                if killed > boss_killer:
                    boss_killer = killed
                    boss_position = [row, col]

    if boss_killer == 0:
        break

    to_kill_row = boss_position[0]
    to_kill_col = boss_position[1]
    matrix[to_kill_row][to_kill_col] = '0'
    result += 1


print(result)