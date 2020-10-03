text = input()

remove_char = 'a o u e i'.split()

for i in remove_char:
    text = text.replace(i, '')

print(text)