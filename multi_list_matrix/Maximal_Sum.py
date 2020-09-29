row, col = list(map(int, input().split()))


def generate_matrix(n, c):
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    return matrix


def max_matrix_element(matrix):
    big = -999
    position_element = None
    for r in range(row - 2):
        for c in range(col - 2):
            m = [
                    [matrix[r][c], matrix[r][c+1], matrix[r][c+2]],
                    [matrix[r+1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]],
                    [matrix[r+2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
                ]

            s = sum(map(sum, m))
            if s > big:
                big = s
                position_element = m

    return big, position_element


matrix = generate_matrix(row, col)

max_number, mat = max_matrix_element(matrix)
print(f'Sum = {max_number}')
for i in mat:
    print(" ".join(str(x) for x in i))
