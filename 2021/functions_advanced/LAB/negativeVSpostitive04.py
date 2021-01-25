def read_input():
    """Read input """
    return input().split()


def convert_to_number():
    return map(int, read_input())


def split_args_to_pos_or_neg():
    args = list(convert_to_number())
    positive = [x for x in args if x > 0]
    negative = [x for x in args if x < 0]
    return positive, negative


def main():
    positive, negative = split_args_to_pos_or_neg()
    negative = sum(negative)
    positive = sum(positive)
    print(negative)
    print(positive)

    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


main()