from collections import deque

number_of_station = int(input())
pumps = deque()

for _ in range(number_of_station):
    pums = [int(x) for x in input().split()]
    pumps.append(pums)


for i in range(number_of_station):
    fuel = 0
    is_valid = True

    for _ in range(number_of_station):
        current = pumps.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        #Always return
        pumps.append(current)

    if is_valid:
        print(i)
        break

    pumps.append(pumps.popleft())


