def read_input():
    """Read input """
    return input().split()


def convert_to_number():
    return map(int, read_input())


def solve():
    """ Return sorted array """
    return sorted(convert_to_number())


print(solve())