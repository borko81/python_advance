efects = [int(x) for x in input().split(', ') if int(x) > 0]
power = [int(x) for x in input().split(', ') if int(x) > 0]

bombs = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}


def check_perfect(bombs):
    return all(x >= 3 for x in bombs.values())


while efects and power and not check_perfect(bombs):
    e = efects[0]
    p = power[-1]

    temp = e + p

    if temp % 3 == 0 and temp % 5 == 0:
        bombs['Crossette Fireworks'] += 1
        efects.pop(0)
        power.pop()
    elif temp % 5 == 0 and temp % 3 != 0:
        bombs['Willow Fireworks'] += 1
        efects.pop(0)
        power.pop()
    elif temp % 5 != 0 and temp % 3 == 0:
        bombs['Palm Fireworks'] += 1
        efects.pop(0)
        power.pop()
    else:
        t = efects.pop(0) - 1
        if t > 0:
            efects.append(t)


if check_perfect(bombs):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if efects:
    print(f"Firework Effects left: {', '.join(str(x) for x in efects)}")

if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

for key, value in bombs.items():
    print(f"{key}: {value}")


'''
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
-------
Congrats! You made the perfect firework show!
Palm Fireworks: 4
Willow Fireworks: 3
Crossette Fireworks: 3
=================================
-15, -8, 0, -16, 0, -22
10, 5
------------------------
Sorry. You can’t make the perfect firework show.
Explosive Power left: 10, 5
Palm Fireworks: 0
Willow Fireworks: 0
Crossette Fireworks: 0

'''