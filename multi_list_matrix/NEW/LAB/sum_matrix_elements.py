x, y = map(int, input().split(', '))

matrix = []

for _ in range(x):
    matrix.append([int(x) for x in input().split(', ')])

print(sum([sum(i) for i in matrix]))
print(matrix)

