def palindrome(word, index=0):
    if word == word[::-1]:
        return '%s is a palindrome' % word
    else:
        return '%s is not a palindrome' % word


print(palindrome("abcba", 0))
print(palindrome("peter", 0))