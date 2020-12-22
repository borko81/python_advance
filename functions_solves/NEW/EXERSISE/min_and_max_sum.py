arguments = [int(x) for x in input().split()]

def solve(args):
    result = ''
    result += f"The minimum number is {min(args)}\n"
    result += f"The maximum number is {max(args)}\n"
    result += f"The sum number is: {sum(args)}\n"
    return result

print(solve(arguments))