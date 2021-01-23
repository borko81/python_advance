from functools import reduce


def multiply_old(*args):
    result = 1
    for a in args:
        result *= a
    return result


def multiply(*args):
    """same but use reduce"""
    return reduce(lambda x, y: x * y, args)


if __name__ == '__main__':
    print(multiply(1, 4, 5))
    print(multiply(4, 5, 6, 1, 3))
    print(multiply(2, 0, 1000, 5000))
