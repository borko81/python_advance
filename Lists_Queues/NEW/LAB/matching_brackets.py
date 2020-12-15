string = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'

result = []

for char in string:
    if char == '(':
        result.append('')

    for i in range(len(result)):
        result[i] += char

    if char == ')':
        word = result.pop()
        print(word)