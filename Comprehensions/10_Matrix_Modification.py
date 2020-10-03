rows = int(input())
OUT = 'END'

matrix = [
    [int(x) for x in input().split()]
    for _ in range(rows)
]

while True:
    command = input().split()
    if command[0] == OUT:
        break

    what, pos1, pos2, pos3 = command
    pos1 = int(pos1)
    pos2 = int(pos2)
    pos3 = int(pos3)

    if 0 <= pos1 < rows and 0 <= pos2 < rows:
        if what == 'Add':
            matrix[pos1][pos2] += pos3
        elif what == 'Subtract':
            matrix[pos1][pos2] -= pos3
    else:
        print('Invalid coordinates')


for i in matrix:
    print(" ".join(str(x) for x in i))
