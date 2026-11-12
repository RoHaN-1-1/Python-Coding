#Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x  = str(x)
        strx = str_x[::-1]
        if x == int(strx):
            return True
        else:
            return False