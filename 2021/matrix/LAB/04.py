rows = int(input())
matrix = [[0] * rows for _ in range(rows)]
position = []

for r in range(rows):
    line = list(input())
    for c in range(rows):
        matrix[r][c] = line[c]

search_symbol = input()

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == search_symbol:
            position.extend([r, c])
            break

if len(position):
    print(tuple(position))
else:
    print(f'{search_symbol} does not occure in matrix')