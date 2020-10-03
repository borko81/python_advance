a, b = map(int, input().split())

matrix = [[] for _ in range(a)]

begin_symbol = 97

for r in range(a):
    for c in range(b):
        temp = chr(begin_symbol + r)
        middle = chr(begin_symbol + r + c)
        result = f'{temp}{middle}{temp}'
        matrix[r].append(result)


for i in matrix:
    print(" ".join(c for c in i))