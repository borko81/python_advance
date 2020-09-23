n, m = map(int, input().split())
total = n + m + 1

a = set()
b = set()

for index in range(1, total):
    if index <= n:
        a.add(int(input()))
    else:
        b.add(int(input()))

result = a & b
for r in result:
    print(r)