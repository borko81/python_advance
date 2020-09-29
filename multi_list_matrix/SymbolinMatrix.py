r_c = int(input())

matrix = []

for _ in range(r_c):
    row = [i for i in input()]
    matrix.append(row)

search_symbol = input()
found = False

for r in range(len(matrix)):
    if found == True:
        break
    for c in range(len(matrix[r])):
        if matrix[r][c] == search_symbol:
            print((r, c))
            found = True
            break

if not found:
    print(f'{search_symbol} does not occur in the matrix')


