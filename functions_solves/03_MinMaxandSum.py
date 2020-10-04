numbers = [int(x) for x in input().split()]


def solve(numbers):
    print(f'The minimum number is {min(numbers)}')
    print(f'The maximum number is {max(numbers)}')
    print(f'The sum number is: {sum(numbers)}')


solve((numbers))