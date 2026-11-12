#Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ls = [-1]
        m = 0
        for i, bracket in enumerate(s):
            if bracket == "(":
                ls.append(i)
            else:
                ls.pop()
                m = max(m,i-ls[-1])
        return m