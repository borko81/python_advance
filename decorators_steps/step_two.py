def get_author(func):
    def wrapper(*args, **kwargs):
        title = func(*args, **kwargs)
        new_title = title + '!!!'
        return new_title
    return wrapper


def get_year(func):
    def wrapper(year):
        if year // 4 == year / 4:
            print(f"The year {year} is highorder")
        else:
            print(f"The year {year} is not highorder")
        return func(year)
    return wrapper


@get_author
@get_year
def get_title(year):
    return "This is the title name"


print(get_title(2021))