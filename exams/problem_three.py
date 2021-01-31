def check_row(result):
    for row in range(len(result)):
        for col in range(len(result[row])):
            if 0 <= col - 1 < len(result[row - 1]) and 0 <= col < len(result[row - 1]):
                result[row][col] = result[row - 1][col - 1] + result[row - 1][col]
    return result


def get_magic_triangle(n: int):
    result = []
    for i in range(1, n + 1):
        result.append([1] * i)
    return check_row(result)


get_magic_triangle(5)