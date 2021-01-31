from collections import deque


def generate_result(in_list):
    result = 0
    for pos, num in enumerate(in_list):
        result += num * pos
    return result


def best_list_pureness(*test):
    l = deque(test[0])
    rotate = test[1]
    max = generate_result(l)
    max_rotation = 0
    for r in range(rotate):
        l.appendleft(l.pop())
        temp_max = generate_result(l)
        if temp_max > max:
            max = temp_max
            max_rotation = r + 1
    return f"Best pureness {max} after {max_rotation} rotations"