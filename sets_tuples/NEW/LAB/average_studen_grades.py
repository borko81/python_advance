number_of_row = int(input())

result = {}

for _ in range(number_of_row):
    name, score = input().split()
    score = "%.2f" % float(score)
    if name not in result:
        result[name] = []
    result[name].append(score)

for name, scores in result.items():
    data = " ".join([str(x) for x in scores])
    scores = [float(x) for x in scores]
    print(f"{name} -> {data} (avg: {(sum(scores) / len(scores)):.2f})")