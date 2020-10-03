n = int(input())

d1 = []
d2 = []

matrix = [
   [int(x) for x in input().split(', ')] for _ in range(n)
]


for i in range(n):
    d2.append(matrix[i][len(matrix) - 1 - i])
    for y in range(n):
        if i == y:
            d1.append(matrix[i][y])


print(f'First diagonal: {", ".join(str(x) for x in d1)}. Sum: {sum(d1)}')
print(f'Second diagonal: {", ".join(str(x) for x in d2)}. Sum: {sum(d2)}')
