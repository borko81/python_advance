from math import floor

size = int(input())
PLAYER = 'P'
WALLS = 'X'

matrix = []
coins = 0
position = []
all_path = []

def show_matrix():
    for row in range(size):
        print(matrix[row])

def validate(matrix, size, x, y):
    return 0 <= x < size and 0 <= y < size and matrix[x][y] != WALLS

for x in range(size):
    matrix.append(input().split())
    if PLAYER in matrix[x]:
        y = matrix[x].index(PLAYER)
        position = [x, y]



while True:
    command = input()
    if command not in ["right", "left", "up", "down"]:
        continue
    if command == "right":
        temp_x = position[0]
        temp_y = position[1] + 1
        if validate(matrix, size,temp_x, temp_y):
            coins += int(matrix[temp_x][temp_y])
            position = [temp_x, temp_y]
            all_path.append(position)
        else:
            coins = floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print('Your path:')
            [print(p) for p in all_path]
            break

    elif command == "left":
        temp_x = position[0]
        temp_y = position[1] - 1
        if validate(matrix, size,temp_x, temp_y):
            coins += int(matrix[temp_x][temp_y])
            position = [temp_x, temp_y]
            all_path.append(position)
        else:
            coins = floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print('Your path:')
            [print(p) for p in all_path]
            break

    elif command == "up":
        temp_x = position[0] - 1
        temp_y = position[1]
        if validate(matrix, size,temp_x, temp_y):
            coins += int(matrix[temp_x][temp_y])
            position = [temp_x, temp_y]
            all_path.append(position)
        else:
            coins = floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print('Your path:')
            [print(p) for p in all_path]
            break

    elif command == "down":
        temp_x = position[0] + 1
        temp_y = position[1]
        if validate(matrix, size,temp_x, temp_y):
            coins += int(matrix[temp_x][temp_y])
            position = [temp_x, temp_y]
            all_path.append(position)
        else:
            coins = floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print('Your path:')
            [print(p) for p in all_path]
            break

    if coins >= 100:
        break


if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
    print("Your path:")
    [print(p) for p in all_path]


'''
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down
----
You won! You've collected 131 coins.
Your path: 
[3, 1]
[3, 2]
[2, 2]
[1, 2]
[1, 1]
[2, 1]
============================
8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left
------------------------
Game over! You've collected 0 coins.
Your path:
[4, 2]

'''