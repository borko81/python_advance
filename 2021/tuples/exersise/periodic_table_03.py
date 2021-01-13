num = int(input())
result = set()

for _ in range(num):
    temp = []
    for element in input().split():
        temp.append(element)
    for t in temp:
        result.add(t)


[print(x) for x in result]