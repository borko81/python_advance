line = input().split()

result = {x: line.count(x) for x in line}

for key, value in result.items():
    print(f"{key} - {value} times")