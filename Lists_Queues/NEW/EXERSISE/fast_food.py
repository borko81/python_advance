#Slow
from collections import deque

total_food = int(input())

orders = deque(int(x) for x in input().split(' '))
complete_task = True
max_order = max(orders)

while orders:
    temp_food = orders[0]

    if temp_food <= total_food:
        total_food -= temp_food
        orders.popleft()

    elif temp_food > total_food:
        complete_task = False
        break


print(max_order)
if complete_task:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")

# Fast
from collections import deque

total = int(input())

orders = deque()


[orders.append(int(i)) for i in input().split(' ')]

m = max(orders)
order_left = deque()
print(m)

while orders:
    check = orders.popleft()
    total -= check
    if total > 0:
        continue
    else:
        order_left.append(check)


if total >= 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in order_left])}")