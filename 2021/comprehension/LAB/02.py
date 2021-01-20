text = input()
vowels = 'a o u e i'.split()


def remove_vowels_from_text(text: str, vowels):
    result = [i for i in text if i not in vowels]
    return "".join(result)


print(remove_vowels_from_text(text, vowels))