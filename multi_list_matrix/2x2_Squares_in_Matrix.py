row, col = list(map(int, input().split()))


def generate_matrix(n, c):
    matrix = [[x for x in input().split()] for _ in range(n)]
    return matrix


def equal_matrix(matrix):
    count = 0
    for r in range(row - 1):
        for c in range(col - 1):
            if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
                count += 1
    return count


matrix = generate_matrix(row, col)
print(equal_matrix(matrix))