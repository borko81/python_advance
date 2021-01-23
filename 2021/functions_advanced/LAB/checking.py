from functools import reduce

a = {
    'test': lambda x, y: x * y,
}

numbers = [1, 2, 3]

print(reduce(a['test'], numbers))