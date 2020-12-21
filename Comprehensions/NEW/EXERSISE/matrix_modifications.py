row = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(row)]


def test_coordinate(matrix, row, col):
    return row > len(matrix) or col > len(matrix) or row < 0 or col < 0


while True:
    command = input()
    if command == 'END':
        break

    command = command.split()

    if command[0] == 'Add':
        row, col, value = map(int, command[1:])
        if not test_coordinate(matrix, row, col):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')

    elif command[0] == 'Subtract':
        row, col, value = map(int, command[1:])
        if not test_coordinate(matrix, row, col):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')

for result in matrix:
    print(' '.join(str(x) for x in result))


