num_of_matrix = int(input())


def write_matrix(num):
    matrix = []
    for i in range(num):
        matrix.append([int(number) for number in input().split(', ')])
    return matrix


def show_only_even(matrix):
    only_even = []
    for i in range(num_of_matrix):
        only_even.append([i for i in matrix[i] if not i % 2])
    return only_even


my_matrix = write_matrix(num_of_matrix)
print(show_only_even(my_matrix))