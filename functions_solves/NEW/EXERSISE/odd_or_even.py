command = input()
arguments = [int(x) for x in input().split()]


def solve(command, arguments):
    if command == 'Even':
        return sum(filter(lambda x: x % 2 == 0, arguments)) * len(arguments)
    elif command == 'Odd':
        return sum(filter(lambda x: x & 1, arguments)) * len(arguments)


print(solve(command, arguments))
