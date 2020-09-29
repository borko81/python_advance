row = int(input())
matrix = []

total = 0
count = 0


for _ in range(row):
    numebrs = [int(x) for x in input().split()]
    matrix.append((numebrs))

for r in range(row):
    total += matrix[r][count]
    count += 1

print(total)