row = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]


print([i for x in matrix for i in x])

print(sum(matrix, []))