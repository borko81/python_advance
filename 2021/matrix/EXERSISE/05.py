from collections import deque

N, M = map(int, input().split())
word = deque(input())

matrix = [[''] * M for _ in range(N)]


for row in range(N):
    for col in range(M):
        current_col = col
        current_char = word.popleft()
        if row % 2:
            current_col = M - 1 - col
        matrix[row][current_col] = current_char
        word.append((current_char))

for i in matrix:
    print("".join(x for x in i))
