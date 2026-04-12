class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        flag = 0
        if x < 0:
            flag = -1
            x *= -1
        for i in range(0,len(str(x)),1):
            y = x // 10
            z = x % 10
            new_num = new_num * 10 + z
            x = y
        if new_num > (2**31)-1:
            return 0
        if flag == -1:
            x *= flag
            return new_num * -1
        return new_num

        ###testing for commit