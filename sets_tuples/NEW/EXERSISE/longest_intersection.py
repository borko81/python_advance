lines = int(input())

result = []

for _ in range(lines):
    row = input().split('-')
    row_one = [int(x) for x in row[0].split(',')]
    row_two = [int(x) for x in row[1].split(',')]

    set_one = set()
    set_two = set()

    for i in range(row_one[0], row_one[1] + 1):
        set_one.add(i)

    for i in range(row_two[0], row_two[1] + 1):
        set_two.add(i)
    check = set_one & set_two
    result.append(list(check))

check_me = sorted(result, key=lambda x: len(x))[-1]

print(f'Longest intersection is {check_me} with length {len(check_me)}')
