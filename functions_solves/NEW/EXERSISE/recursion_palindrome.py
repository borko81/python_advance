def palindrome(word, index=0):
    if word == "".join(reversed(word)):
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))