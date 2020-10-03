row_of_matrix = int(input())


def create_matrix(row_of_matrix):
    matrix = [[int(x) for x in input().split(',')] for _ in range(row_of_matrix)]
    return matrix


matrix = create_matrix((row_of_matrix))


for i in range(row_of_matrix):
    for j in range(len(matrix[i])):
        target = matrix[i][j]
        if target & 1:
            matrix[i][j] = ''


print([[i for i in z if i != ''] for z in matrix])


