row, col = list(map(int, input().split()))


def generate_matrix(n):
    generate_matrix_me = [[x for x in input().split()] for _ in range(n)]
    return generate_matrix_me


def print_matrix_result(my_matrix):
    for i in my_matrix:
        print(" ".join(str(x) for x in i))


matrix = generate_matrix(row)

while True:
    tokens = input().split()
    if tokens[0] == 'END':
        break

    if tokens[0] == 'swap' and len(tokens) == 5:
        row1, col1, row2, col2 = map(int, tokens[1:])
        if row1 in range(row) and row2 in range(row) and col1 in range(col) and col2 in range(col):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print_matrix_result(matrix)
        else:
            print('Invalid input!')

    else:
        print('Invalid input!')
