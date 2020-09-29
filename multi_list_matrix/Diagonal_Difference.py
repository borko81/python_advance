row = int(input())


def generate_matrix(n):
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    return matrix


def take_l_diagonal(matrix):
    result = 0
    for r in range(len(matrix)):
        result += matrix[r][r]
    return result


def take_r_diagonal(matrix):
    result = 0
    temp = len(matrix) - 1
    for r in range(len(matrix)):
        result += matrix[r][temp - r]
    return result


matrix = generate_matrix(row)
print(abs(take_l_diagonal(matrix) - take_r_diagonal(matrix)))