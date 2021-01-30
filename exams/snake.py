def read_input():
    row = int(input())
    matrix = [
        list(input()) for _ in range(row)
    ]
    return matrix, row


def found_position(matrix, search):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == search:
                return r, c


def check_valid_coordinate(row, x, y, nx, ny):
    return 0 <= x + nx < row and 0 <= y + ny < row


def print_matrix(matrix):
    for x in matrix:
        print("".join(x))


moove_position = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

food = 0

matrix, row = read_input()
snake_position_x, snake_position_y = found_position(matrix, 'S')
finish = False

while not finish:
    command = input()
    nx, ny = moove_position[command]
    matrix[snake_position_x][snake_position_y] = '.'

    if not check_valid_coordinate(row, snake_position_x, snake_position_y, nx, ny):
        print("Game over!")
        print(f"Food eaten: {food}")
        finish = True
        break

    snake_position_x = snake_position_x + nx
    snake_position_y = snake_position_y + ny

    if matrix[snake_position_x][snake_position_y] == '*':
        matrix[snake_position_x][snake_position_y] = 'S'
        food += 1
        if food >= 10:
            print("You won! You fed the snake.")
            print(f"Food eaten: {food}")
            finish = True
            break
    elif matrix[snake_position_x][snake_position_y] == 'B':
        matrix[snake_position_x][snake_position_y] = '.'
        b_x, b_y = found_position(matrix, 'B')
        snake_position_x = b_x
        snake_position_y = b_y
        matrix[snake_position_x][snake_position_y] = 'S'
    else:
        matrix[snake_position_x][snake_position_y] = 'S'

print_matrix(matrix)