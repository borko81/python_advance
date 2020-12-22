arguments = [int(x) for x in input().split()]

def solve(args):
    return list(filter(lambda x: x % 2 == 0, args))

print(solve(arguments))