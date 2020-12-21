from functools import reduce


def operate(param, *args):
    if param == '+':
        return sum(args)
    elif param == '-':
        return reduce(lambda x, y: x - y, args)
    elif param == '*':
        return reduce(lambda x, y: x * y, args)
    elif param == '/':
        try:
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError as e:
            return e
    elif param == '//':
        try:
            return reduce(lambda x, y: x // y, args)
        except ZeroDivisionError as e:
            return e


print(operate("+", 1, 2, 3))
print(operate("*", 3, 0))

# from functools import reduce
#
# params = {
#     '+': lambda x, y: x + y,
#     '*': lambda x, y: x * y,
# }
#
#
# def operate(param, *args):
#     return eval(params[param]([str(x) for x in args]))
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 0))