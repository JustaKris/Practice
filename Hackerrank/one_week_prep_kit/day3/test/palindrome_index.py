def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        new_word = s[:i] + s[i + 1:]
        if new_word == new_word[::-1]:
            return i
    return -1


# Test Cases
print(palindromeIndex("aaab"))
print(palindromeIndex("baa"))
print(palindromeIndex("aaa"))
print(palindromeIndex("abc"))
