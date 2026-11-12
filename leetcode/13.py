#Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and numbers[s[i]] < numbers[s[i+1]]:
                ans -= numbers[s[i]]
            else:
                ans += numbers[s[i]]
        
        return ans