def read_input():
    """Read input """
    return input().split()


def convert_to_number():
    """Convert to number """
    return map(int, read_input())


def solve():
    """ Solve problems """
    args = convert_to_number()
    return [x for x in args if not x % 2]


print(solve())