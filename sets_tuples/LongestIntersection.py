n_rows = int(input())

result = []
m = -999

for _ in range(n_rows):
    token = input()
    f_start, f_end = map(int, token.split('-')[0].split(','))
    s_start, s_end = map(int, token.split('-')[1].split(','))

    a = set([i for i in range(f_start, f_end+1)])
    b = set([i for i in range(s_start, s_end+1)])

    check = (a & b)
    if len(check) > m:
        m = len(check)
        result.append(check)


print(f'Longest intersection is {list(result[-1])} with length {m}')
