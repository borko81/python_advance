matrix_row = int(input())


def write_matrix():
    temp = []
    for row in range(matrix_row):
        temp.append([i for i in input().split(', ')])
    return temp


def flattern_matrix():
    matrix = write_matrix()
    #return [int(i) for m in matrix for i in m]
    return [int(x) for x in sum(matrix, [])]


print(flattern_matrix())