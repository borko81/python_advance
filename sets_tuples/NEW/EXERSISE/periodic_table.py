n = int(input())
elements = set()

for _ in range(n):
    for e in input().split():
        elements.add(e)

[print(x) for x in elements]