import itertools
numbers = [x for x in input().split(', ')]
n = len(numbers)
# result = set(itertools.permutations(['-'] * n + ['+'] * n, n))
#
# for l in list(result):
#     expr = itertools.chain(*zip(l, numbers))
#     result = "".join(expr)
#     print(f"{result}={eval(result)}")

result = [x for x in (itertools.product('+-', repeat=n))]
for l in result:
    expr = itertools.chain(*zip(l, numbers))
    result = "".join(expr)
    print(f"{result}={eval(result)}")
