clots = [int(x) for x in input().split()]
capacity = int(input())
needed = 0
temp = 0

while clots:
    current = clots[-1]
    if capacity >= temp + current:
        temp += clots.pop()
    else:
        temp = 0
        needed += 1

if temp > 0:
    needed += 1

print(needed)
