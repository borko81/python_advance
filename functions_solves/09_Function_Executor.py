def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    store_result = []

    for f in args:
        func = f[0]
        numbers = f[1]

        result = func(*numbers)
        store_result.append(result)

    return store_result




print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))