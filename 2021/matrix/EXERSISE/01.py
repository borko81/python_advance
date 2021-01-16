rows = int(input())

matrix = [[0] * rows for _ in range(rows)]

left = 0
right = 0

for r in range(rows):
    line = [int(x) for x in input().split()]
    for c in range(len(line)):
        matrix[r][c] = line[c]
        if r == c:
            left += matrix[r][c]
        if c == rows - r - 1:
            right += matrix[r][c]


print(abs(left - right))