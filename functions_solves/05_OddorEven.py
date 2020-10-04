command = input()
numbers = [int(x) for x in input().split()]

check = {
    'Odd': sum([i for i in numbers if i % 2]),
    'Even': sum([i for i in numbers if i % 2 == 0]),
}


def solve():
    l = len(numbers)
    return check[command] * l


print(solve())

