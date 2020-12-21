line = [x.strip() for x in input().split('|')]
result = list(reversed([x.split() for x in line]))

print(" ".join([x for temp in result for x in temp]))