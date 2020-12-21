###1
row = int(input())

matrix = [[int(i) for i in input().split(', ')] for _ in range(row)]

f = []
s = []

for x in range(row):
    for y in range(row):
        if x == y:
            f.append(matrix[x][y])
        if x == row - y - 1:
            s.append(matrix[x][y])


print(f'First diagonal: {", ".join(str(x) for x in f)}. Sum: {sum(f)}')
print(f'Second diagonal: {", ".join(str(x) for x in s)}. Sum: {sum(s)}')

###2
# row = int(input())
#
# matrix = []
#
# for _ in range(row):
#     matrix.append([int(x) for x in input().split(',')])
#
#
# def first():
#     return [matrix[x][y] for x in range(row) for y in range(row) if x == y ]
#
#
# def second():
#     return [matrix[x][y] for x in range(row) for y in range(row) if x == row - y - 1]
#
# f = first()
# s = second()
# print(f'First diagonal: {", ".join(str(x) for x in f)}. Sum: {sum(f)}')
# print(f'Second diagonal: {", ".join(str(x) for x in s)}. Sum: {sum(s)}')

###3
# n = int(input())
#
# d1 = []
# d2 = []
#
# matrix = [
#    [int(x) for x in input().split(', ')] for _ in range(n)
# ]
#
#
# for i in range(n):
#     d2.append(matrix[i][len(matrix) - 1 - i])
#     for y in range(n):
#         if i == y:
#             d1.append(matrix[i][y])
#
#
# print(f'First diagonal: {", ".join(str(x) for x in d1)}. Sum: {sum(d1)}')
# print(f'Second diagonal: {", ".join(str(x) for x in d2)}. Sum: {sum(d2)}')