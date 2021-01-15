def search_for_max(m, x, y):
    position = [[m[x][y], m[x][y+1]], [m[x+1][y],  m[x+1][y+1]]]
    return m[x][y] + m[x][y+1] + m[x+1][y] + m[x+1][y+1], position


x_top, y_top = map(int, input().split(', '))

matrix = []

for _ in range(x_top):
    matrix.append([int(x) for x in input().split(', ')])

max = -999
maximum_element = []

for x in range(x_top - 1):
    for y in range(y_top - 1):
        temp, position = search_for_max(matrix, x, y)
        if temp > max:
            max = temp
            maximum_element = position


for i in maximum_element:
    print(" ".join([str(x) for x in i]))

print(max)
