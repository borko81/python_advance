num = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(num)]

result = [[x for x in i if x % 2 == 0] for i in matrix]

print(result)
