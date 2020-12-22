arguments = [int(x) for x in input().split()]


def show_output(negative, positive):
    return "The negatives are stronger than the positives" if abs(negative) > positive else \
        "The positives are stronger than the negatives"


def solve(args):
    negative = [i for i in args if i < 0]
    positive = [i for i in args if i not in negative]
    temp_negative = sum(negative)
    temp_positive = sum(positive)
    result = ''
    result += f"{temp_negative}\n"
    result += f"{temp_positive}\n"
    result += show_output(temp_negative, temp_positive)
    return result


print(solve(arguments))

#2
numbers = [int(x) for x in input().split(' ')]


def solve(numbers):
    positive = sum(filter(lambda x: x>=0, numbers))
    negative = sum(filter(lambda x: x<0, numbers))
    print(negative)
    print(positive)
    if abs(negative) > positive:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


solve(numbers)