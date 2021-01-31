size = 8


def generate_matrix():
    matrix = []
    for _ in range(8):
        matrix.append(input().split())
    return matrix


def show_matrix(matrix):
    for r in range(8):
        print(" ".join(matrix[r]))


def check_is_valid_position(size, x , y, matrix):
    return 0 <= x < size and 0 <= y < size and matrix[x][y] != 'Q'


def next_position(old_x, old_y, new_x, new_y):
    new_r = old_x + new_x
    new_c = old_y + new_y
    return new_r, new_c


mooves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'a': (-1, -1),
    'b': (-1, 1),
    'c': (1, -1),
    'd': (1, 1)
}
result = []

matrix = generate_matrix()

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'Q':
            for key, moove in mooves.items():
                new_r = r + moove[0]
                new_c = c + moove[1]
                while check_is_valid_position(size, new_r, new_c, matrix):
                    if matrix[new_r][new_c] == 'K':
                        result.append([r, c])
                    new_r += moove[0]
                    new_c += moove[1]


if result:
    [print(x) for x in result]
else:
    print("The king is safe!")