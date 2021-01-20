start = int(input())
end = int(input())

range_for_test = range(2, 11)


def check_if_numer_divide(test_range):
    list_with_number = range(start, end + 1)
    return [i for i in list_with_number if any(i % k == 0 for k in range_for_test)]


print(check_if_numer_divide(range_for_test))