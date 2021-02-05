def check_validate_line(matrix, row, col):
    len_of_row = len(matrix[row]) - 1
    return 0 <= col - 1 < len_of_row and 0 <= col < len_of_row


def get_magic_triangle(n: int):
    result = [[1] * i for i in range(1, n + 1)]
    for i in range(1, n):
        for col in range(len(result[i])):
            if check_validate_line(result, i, col):
                result[i][col] = result[i - 1][col] + result[i - 1][col - 1]
    return result


print(get_magic_triangle(5))
