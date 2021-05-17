from functools import wraps


def show_year(year):
    def add_year(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"The year {year}")
            return func(*args, **kwargs)

        return wrapper

    return add_year


@show_year(2021)
def show_message(message):
    return "The message is {}".format(message)


print(show_message.__name__)
print(show_message('borko'))
