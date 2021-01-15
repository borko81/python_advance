from typing import Set

len_a, len_b = map(int, input().split())


def insert_element(l: int) -> Set:
    result = set()
    for _ in range(l):
        result.add(input())
    return result


first_items = set(insert_element(len_a))
second_items = set(insert_element(len_b))

[print(int(x)) for x in list(first_items & second_items)]

