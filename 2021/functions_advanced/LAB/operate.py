from functools import reduce


def operate_old(operator, *args):
    """ Using eval"""
    try:
        return eval(f"{operator}".join(str(x) for x in args))
    except ZeroDivisionError as e:
        return e


operators_data = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '//': lambda x, y: x // y,
}


def operate(operator, *args):
    """ Using lambda through reduce """
    try:
        return reduce(operators_data[operator], args)
    except ZeroDivisionError as e:
        print(e)


print(operate("+", 1, 2, 3))
print(operate("/", 3, 1))
