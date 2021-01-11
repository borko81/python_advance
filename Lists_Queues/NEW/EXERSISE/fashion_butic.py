clothes = [int(x) for x in input().split()]
size = int(input())

rack = 0
get_clothes = 0

while clothes:
    temp = clothes[-1]

    if get_clothes + temp <= size:
        get_clothes += clothes.pop()
    else:
        get_clothes = 0
        rack += 1

# If have more in rack += 1
if get_clothes > 0:
    rack += 1

print(rack)
