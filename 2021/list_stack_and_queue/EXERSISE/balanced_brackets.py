test = '{[(])}'
brackets = {
    '[': ']',
    '(': ')',
    '{': '}'
}

result = []
OK = True


for i in test:
    if i in brackets.keys():
        result.append(i)
    elif i in brackets.values() and result:
        temp = result.pop()
        if i != brackets[temp]:
            OK = False
            print('NO')
            break

if OK:
    print('YES')
