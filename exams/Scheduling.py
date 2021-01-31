from collections import deque

numbers = deque([int(x) for x in input().split(', ')])
index = int(input())

sorted_numbers = sorted(set(numbers))

total_cicle = 0
exit = False

for pos_x, x in enumerate(sorted_numbers):
    if exit:
        break
    for pos_y, y in enumerate(numbers):
        if x == y:
            total_cicle += y
            if pos_y == index:
                exit = True
                break


print(total_cicle)