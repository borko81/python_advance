row, col = [int(x) for x in input().split(' ')]

matrix = []

for _ in range(row):
    matrix.append([x for x in input().split(' ')])

action = []

while True:
    command = input()
    if command == 'END':
        break
    else:
        action.append((command))

for c in action:
    if c.startswith('swap') and len(c.split(' ')) == 5:
        o, oo, t, tt = [int(x) for x in c.split(' ')[1:]]
        try:
            matrix[o][oo], matrix[t][tt] = matrix[t][tt], matrix[o][oo]
        except:
            print('Invalid input!')
        else:
            [print(" ".join(x)) for x in matrix]
    else:
        print('Invalid input!')