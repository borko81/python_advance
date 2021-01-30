def numbers_searching(*args):
    result = []
    temp_list = list(args).copy()
    temp_list = set([x for x in temp_list if temp_list.count(x) > 1])
    duplicate_numbers = list(sorted(temp_list))
    missing_number = set([i for i in range(min(args), max(args) + 1)]) - set(args)
    result.append(list(missing_number)[0])
    result.append(duplicate_numbers)
    return result



print(numbers_searching(1, 2, 4, 2, 5, 4))                                          # [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))                                   # [6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))# [46, [44, 45, 47, 48, 50]]