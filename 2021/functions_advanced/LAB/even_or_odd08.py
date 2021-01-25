data = {
    'even': lambda x: x % 2 == 0,
    'odd': lambda x: x % 2
}


def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command in data:
        return list(filter(data[command], numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))