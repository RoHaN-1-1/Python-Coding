#Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if s[0] == "}" or s[0] == ")" or s[0] == "]":
            return False
        brackets = []
        for i in range(0,len(s),1):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                brackets.append(s[i])
            elif s[i] == "}" and len(brackets) != 0:
                if brackets[-1] == "{":
                    brackets.pop()
                else:
                    return False
            elif s[i] == ")" and len(brackets) != 0:
                if brackets[-1] == "(":
                    brackets.pop()
                else:
                    return False
            elif s[i] == "]" and len(brackets) != 0:
                if brackets[-1] == "[":
                    brackets.pop()
                else:
                    return False
            else:
                return False
        if len(brackets) == 0:
            return True
        else:
            return False
        