row, col = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(row)]


def show_matrix(matrix):
    for fun_row in matrix:
        print(" ".join(str(x) for x in fun_row))


while True:
    command = input()
    if command == 'END':
        break
    elif command.startswith('swap') and len(command.split()) == 5:
        a, b, c, d = map(int, command.split()[1:])
        if a in range(row) and b in range(row) and c in range(col) and d in range(col):
            matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]
            show_matrix(matrix)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
