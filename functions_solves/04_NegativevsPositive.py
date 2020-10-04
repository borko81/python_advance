numbers = [int(x) for x in input().split()]


def solve(numbers):
    p_numbers = 0
    n_numbers = 0
    for i in numbers:
        if i > 0:
            p_numbers += i
        else:
            n_numbers += i

    print(n_numbers)
    print(p_numbers)
    if abs(p_numbers) > abs(n_numbers):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


solve(numbers)