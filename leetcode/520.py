# class Solution:
def detectCapitalUse(word):
    if word.isupper():
        return True
    if word.islower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False
word = "Google"
print(detectCapitalUse(word))