from collections import deque

N, M = map(int, input().split())
word = deque(input())

matrix = []

for n in range(N):
    matrix.append([])
    for m in range(M):
        matrix[n].append('')


for row in range(N):
    for col in range(M):
        current_col = col
        current_char = word.popleft()
        if row % 2 != 0:
            current_col = M - 1 - col
        matrix[row][current_col] = current_char
        word.append((current_char))

for i in matrix:
    print("".join(x for x in i))

