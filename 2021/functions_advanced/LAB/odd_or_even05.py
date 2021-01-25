def get_input():
    command = input()
    numbers = map(int, input().split())
    return command, list(numbers)


def solve():
    command, numbers = get_input()
    len_of_numbers = len(numbers)

    if command == 'Odd':
        return sum([x for x in numbers if x % 2]) * len_of_numbers
    return sum([x for x in numbers if not x % 2]) * len_of_numbers


print(solve())