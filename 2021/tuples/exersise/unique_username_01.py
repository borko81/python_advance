num_of_rows = int(input())

names = set()
for _ in range(num_of_rows):
    names.add(input())

[print(x) for x in names]