from collections import deque

childrens = deque(input().split())
n = int(input())

# solve
while len(childrens) != 1:
    for i in range(n):
        if i == n - 1:
            print(f"Removed {childrens.popleft()}")
            break
        childrens.append(childrens.popleft())

print(f"Last is {childrens[0]}")

