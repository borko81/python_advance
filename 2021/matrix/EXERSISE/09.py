def find_player_position(matrix):
    ''' Search for player posiiton '''
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                return r, c


def find_bunny_position(matrix):
    ''' Search for bunnys positions '''
    bunnys = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                bunnys.append([r, c])
    return bunnys


def check_corect_position(matrix, x, y, row, col):
    '''
        Check posiiton is ok in matrix or not,
        in function use x +- 1 or y +=1
    '''
    return 0 <= x < row and 0 <= y < col


def show_matrix(matrix):
    ''' Print matrix '''
    for r in range(row):
        print("".join(matrix[r]))


def bunny_grow(matrix, new_x, new_y, row, col):
    '''
        Increase bunnys, use global param dead, to return if bunny move to player after grow
    '''
    global dead
    if check_corect_position(matrix, new_x + 1, new_y, row, col):
        if matrix[new_x + 1][new_y] == 'P':
            print(f"dead: {new_x + 1} {new_y}")
            dead = True
        matrix[new_x + 1][new_y] = 'B'

    if check_corect_position(matrix, new_x - 1, new_y, row, col):
        if matrix[new_x - 1][new_y] == 'P':
            print(f"dead: {new_x - 1} {new_y}")
            dead = True
        matrix[new_x - 1][new_y] = 'B'

    if check_corect_position(matrix, new_x, new_y + 1, row, col):
        if matrix[new_x][new_y + 1] == 'P':
            print(f"dead: {new_x} {new_y + 1}")
            dead = True
        matrix[new_x][new_y + 1] = 'B'

    if check_corect_position(matrix, new_x, new_y - 1, row, col):
        if matrix[new_x][new_y - 1] == 'P':
            print(f"dead: {new_x} {new_y - 1}")
            dead = True
        matrix[new_x][new_y - 1] = 'B'

    return matrix


def bunny_grow_in_cyckle(matrix):
    '''
        For every bunny in bunnyes push bunny_grow function
    '''
    for bunny in find_bunny_position(matrix):
        bunny_x = bunny[0]
        bunny_y = bunny[1]
        matrix = bunny_grow(matrix, bunny_x, bunny_y, row, col)


# Hard code moves
positions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

# Read input's
row, col = map(int, input().split())
matrix = []
dead = False
escape = False

for matrix_insert in range(row):
    matrix.append(list(input()))

commands = list(input())

player_position_x, player_position_y = find_player_position(matrix)

for command in commands:
    if not dead and not escape:
        temp_moove = positions[command]
        if 0 <= player_position_x + temp_moove[0] < row and 0 <= player_position_y + temp_moove[1] < col:
            matrix[player_position_x][player_position_y] = '.'
            player_position_x += temp_moove[0]
            player_position_y += temp_moove[1]

            if matrix[player_position_x][player_position_y] == 'B':
                bunny_grow_in_cyckle(matrix)
                show_matrix(matrix)
                print(f"dead: {player_position_x} {player_position_y}")
                break
            else:
                matrix[player_position_x][player_position_y] = 'P'
                bunny_grow_in_cyckle(matrix)
                if dead:
                    show_matrix(matrix)
                    break

        else:
            matrix[player_position_x][player_position_y] = '.'
            bunny_grow_in_cyckle(matrix)
            show_matrix(matrix)
            print(f"won: {player_position_x} {player_position_y}")
            # Players escape, but game has more turns!
            escape = True
