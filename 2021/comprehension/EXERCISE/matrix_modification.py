number_of_rows = int(input())


def generate_matrix(number_of_rows):
    '''Generate matrix'''
    matrxi = [
        [int(x) for x in input().split()] for _ in range(number_of_rows)
    ]
    return matrxi


def check_cords_is_ok(number_of_rows, x, y):
    '''Check for valid coorinates'''
    return 0 <= x < number_of_rows and 0 <= y < number_of_rows


def check_command_of_input(matrix, x, y, command):
    '''Logic is here'''
    if command == 'Add':
        matrix[x][y] += value
        return matrix
    elif command == "Subtract":
        matrix[x][y] -= value
        return matrix


def show_line_of_matrix(matrix):
    '''Show matrix'''
    for r in range(number_of_rows):
        print(' '.join(str(x) for x in matrix[r]))


# Assign function generate matrix to variable matrix
matrix = generate_matrix(number_of_rows)

while True:
    command = input()
    if command == 'END':
        break
    line = command.split()
    comma = line[0]
    x = int(line[1])
    y = int(line[2])
    value = int(line[3])
    if check_cords_is_ok(number_of_rows, x, y):
        matrix = check_command_of_input(matrix, x, y, comma)
    else:
        print("Invalid coordinates")


show_line_of_matrix(matrix)