
num_of_lines = int(input())
max_l = -999
result = set()

for _ in range(num_of_lines):
    line = input()
    a, b = line.split('-')
    first_start, first_end = map(int, a.split(','))
    second_start, second_end = map(int, b.split(','))
    first = set([i for i in range(first_start, first_end + 1)])
    second = set([i for i in range(second_start, second_end + 1)])
    check = first & second
    if len(check) > max_l:
        max_l = len(check)
        result = check

elements = ", ".join(str(x) for x in result)
print(f"Longest intersection is [{elements}] with length {max_l}")
