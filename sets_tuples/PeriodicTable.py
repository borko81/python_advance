line_count = int(input())

elements = set()

for _ in range(line_count):
    element = input().split()
    for e in element:
        elements.add(e)


[print(e) for e in elements]
