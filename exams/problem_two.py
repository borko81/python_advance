def show_matrix(matrix):
    for row in range(len(matrix)):
        print("".join(matrix[row]))


def generate_matrix(row):
    matrix = []
    for _ in range(row):
        matrix.append(list(input()))
    return matrix


def is_valid_coordinate(x, y, new_x, new_y, size):
    return 0 <= x + new_x < size and 0 <= y + new_y < size


def find_person_position(matrix, size):
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 'P':
                return x, y


moove = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

string = input()
row = int(input())

matrix = generate_matrix(row)
num_of_command = int(input())
x, y = find_person_position(matrix, row)

for _ in range(num_of_command):
    command = input()
    new_x, new_y = moove[command]
    if is_valid_coordinate(x, y, new_x, new_y, row):
        matrix[x][y] = '-'
        x += new_x
        y += new_y
        if matrix[x][y].isalpha():
            string += matrix[x][y]
        matrix[x][y] = 'P'
    else:
        string = string[:-1]

print(string)
show_matrix(matrix)