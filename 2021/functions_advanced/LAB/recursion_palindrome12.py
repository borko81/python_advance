def req_palindrome_check(word):
    if len(word) == 0:
        return word
    return req_palindrome_check(word[1:]) + word[0]


def palindrome(word, index):
    if word == req_palindrome_check(word):
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))