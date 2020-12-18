x_top, y_top = map(int, input().split(', '))

matrix = []

for _ in range(x_top):
    matrix.append([int(x) for x in input().split(', ')])

max = -999
maximum_element = []

for x in range(x_top - 1):
    for y in range(y_top - 1):
        a = matrix[x][y]
        b = matrix[x][y+1]
        c = matrix[x+1][y]
        d = matrix[x+1][y+1]
        if a + b + c + d > max:
            max = a + b + c + d
            maximum_element = [[a, b], [c, d]]


for i in maximum_element:
    print(" ".join([str(x) for x in i]))

print(max)
