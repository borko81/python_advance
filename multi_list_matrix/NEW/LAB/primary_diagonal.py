row = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(row)]

check_sum = 0

for x in range(len(matrix)):
    for y in range(row):
        if x == y:
            check_sum += matrix[x][y]

print(check_sum)
