def read_input():
    """Read input """
    return input().split()


def convert_to_number():
    return map(int, read_input())


def main():
    args = list(convert_to_number())
    print(f"The minimum number is {min(args)}")
    print(f"The maximum number is {max(args)}")
    print(f"The sum number is: {sum(args)}")


main()