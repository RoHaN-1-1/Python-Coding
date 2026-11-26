#Minimize Maximum of Array
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        total = 0
        ans = 0

        for i in range(0,len(nums)):
            total += nums[i]

            avg = (total + i)//(i+1)
            ans = max(ans,avg)

        return ans