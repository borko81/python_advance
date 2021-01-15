rows = int(input())

matrix = [[0] * rows for _ in range(rows)]
sum_diagonal: int = 0

for r in range(rows):
    line = [int(x) for x in input().split(' ')]
    for c in range(rows):
        matrix[r][c] = line[c]
        if r == c:
            sum_diagonal += line[c]

print(sum_diagonal)