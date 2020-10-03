collection = input().split('|')

temp = [i.split() for i in collection]
result = []

for t in temp[::-1]:
    result.extend([int(x) for x in t])

print(" ".join(str(x) for x in result))
