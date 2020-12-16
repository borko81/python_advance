def solve():
    check = input()
    pos = []
    result = True

    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for _ in check:
        if _ in "({[":
            pos.append(_)
        elif _ in ")}]":
            if pos:
                c = pos[-1]
                if d[c] == _:
                    pos.pop()
                else:
                    result = False
                    break
            else:
                result = False
                break

    if result:
        print('YES')
    else:
        print('NO')


solve()