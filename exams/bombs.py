from collections import deque

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

total_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}


def read_input():
    return [int(x) for x in input().split(', ')]


def check_is_three():
    return all([b >= 3 for b in total_bombs.values()])


bombs_effects = deque(read_input())
bombs_casing = deque(read_input())

while bombs_effects and bombs_casing and not check_is_three():
    efect = bombs_effects[0]
    casing = bombs_casing[-1]
    total = efect + casing
    if total in bombs:
        total_bombs[bombs[total]] += 1
        bombs_effects.popleft()
        bombs_casing.pop()

    else:
        bombs_casing[-1] -= 5

if check_is_three():
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bombs_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bombs_effects)}")

if not bombs_casing:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bombs_casing)}")

for key, value in sorted(total_bombs.items()):
    print(f"{key}: {value}")