n = int(input())
commands = input().split()
next_position = {
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1),
    'down': (1, 0),
}

matrix = []

for f_row in range(n):
    matrix.append(input().split())


def obhod_matrix(matr, search):
    for matr_x in range(n):
        for matr_y in range(n):
            if matr[matr_x][matr_y] == search:
                return x, y
    return "No more coal"


start_position = obhod_matrix(matrix, 's')
coal = 0
x, y = map(int, start_position)


def find_total_coal():
    temp = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'c':
                temp += 1
    return temp


total_coal = find_total_coal()

for command in range(len(commands)):
    next_x, next_y = next_position[commands[command]]
    if 0 <= x + next_x < n and 0 <= y + next_y < n:

        matrix[x][y] = '*'
        x = x + next_x
        y = y + next_y

        if matrix[x][y] == 'c':
            coal += 1
            matrix[x][y] = '*'
            if obhod_matrix(matrix, 'c') == "No more coal":
                print("You collected all coals! ({x}, {y})".format(x=x, y=y))
                break
        elif matrix[x][y] == 'e':
            print("Game over! ({x}, {y})".format(x=x, y=y))
            break
    if command + 1 == len(commands):
        print("{coal_left} coals left. ({x}, {y})".format(coal_left=total_coal-coal, x=x, y=y))
