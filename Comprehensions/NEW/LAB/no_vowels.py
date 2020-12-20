vowels = 'a, o, u, e, i'.split(', ')
text = [x for x in input() if x not in vowels]

print("".join(text))