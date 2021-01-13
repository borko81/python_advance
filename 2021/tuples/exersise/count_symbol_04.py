text = input()
result = {i:text.count(i) for i in text}

for key, value in sorted(result.items()):
    print(f"{key}: {value} time/s")