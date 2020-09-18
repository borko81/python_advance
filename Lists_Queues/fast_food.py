from collections import deque

total_qty = int(input())
orders = [int(x) for x in input().split()]

print(max(orders))


while orders:
    val = orders[0]
    if val <= total_qty:
        total_qty -= val
        orders.pop(0)
    else:
        break


if len(orders) == 0:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(str(i) for i in orders)}')


