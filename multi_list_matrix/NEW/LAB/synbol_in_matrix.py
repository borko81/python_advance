row = int(input())

matrix = [[x for x in input()] for _ in range(row)]

search_symbol = input()
found = False

for x in range(len(matrix)):
    if found:
        break
    for y in range(len(matrix[x])):
        if search_symbol == matrix[x][y]:
            print(f"({x}, {y})")
            found = True
            break

if not found:
    print(f"{search_symbol} does not occur in the matrix")
