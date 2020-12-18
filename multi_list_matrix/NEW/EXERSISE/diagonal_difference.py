n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]


l = 0
r = 0

for x in range(n):
    for y in range(n):
        if x == y:
            l += matrix[x][y]
        if x == n - y - 1:
            r += matrix[x][y]

print(abs(l - r))