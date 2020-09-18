p = input()

brackets = []
OK = True

for i in p:
    if i == '{':
        brackets.append(i)
    elif i == '(':
        brackets.append(i)
    elif i == '[':
        brackets.append(i)
    elif i == '}' and len(brackets) > 0 and brackets[-1] == '{':
        brackets.pop()
    elif i == ')' and len(brackets) > 0 and brackets[-1] == '(':
        brackets.pop()
    elif i == ']' and len(brackets) > 0 and brackets[-1] == '[':
        brackets.pop()
    else:
        OK = False

if OK:
    print('YES')
else:
    print('NO')