text = input()

result = {x: text.count(x) for x in text}

for k, v in sorted(result.items()):
    print(f"{k}: {v} time/s")