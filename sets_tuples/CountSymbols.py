text = input()

result = {i:text.count(i) for i in text}

for k, v in sorted(result.items()):
    print(f'{k}: {v} time/s')