from collections import deque

childred = deque(input().split())
n = int(input())
index = 0

while len(childred) != 1:
    index += 1
    person = childred.popleft()
    if index % n == 0:
        print(f'Removed {person}')
    else:
        childred.append(person)

print(f'Last is {childred[0]}')
