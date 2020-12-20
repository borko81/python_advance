num = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(num)]

print([x for l in matrix for x in l])