row, col = map(int, input().split(', '))
matrix = [[int(x) for x in input().split()] for _ in range(row)]
[print(r) for r in [sum(i) for i in zip(*matrix)]]

