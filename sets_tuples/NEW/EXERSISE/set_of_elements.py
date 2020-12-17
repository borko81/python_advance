n, m = map(int, input().split())

first = set()
second = set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

[print(x) for x in first & second]