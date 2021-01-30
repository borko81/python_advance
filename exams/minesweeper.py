def show_matrix():
    for r in range(size):
        print(" ".join(str(x) for x in matrix[r]))


def validate_position(x, y, dx, dy, sizeme):
    return 0 <= x + dx < sizeme and 0 <= y + dy < sizeme


def calc_bombs(x, y, dx, dy, matrix):
    if matrix[x + dx][y + dy] == '*':
        return 1
    return 0


moove = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "a": (-1, -1),
    "b": (-1, 1),
    "c": (1, -1),
    "d": (1, 1),
}


size = int(input())
bombs = int(input())

matrix = [
    [0] * size for _ in range(size)
]

def add_bombs_to_position():
    for _ in range(bombs):
        line = input()
        line = line.replace('(', '')
        line = line.replace(')', '')
        x, y = line.split(', ')
        x = int(x)
        y = int(y)
        matrix[x][y] = '*'


def generate_result():
    for row_matrix in range(size):
        for col_matrix in range(size):
            if matrix[row_matrix][col_matrix] != '*':
                temp_count = 0
                for key, value in moove.items():
                    if validate_position(row_matrix, col_matrix, value[0], value[1], size):
                        temp_count += calc_bombs(row_matrix, col_matrix, value[0], value[1], matrix)
                matrix[row_matrix][col_matrix] = temp_count


def main():
    add_bombs_to_position()
    generate_result()
    show_matrix()

main()
