#Longest Strictly Increasing or Strictly Decreasing Subarray
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inr = 1
        dcr = 1
        ans = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inr += 1
                dcr = 1

            elif nums[i] < nums[i - 1]:
                dcr += 1
                inr = 1

            else:
                inr = 1
                dcr = 1

            ans = max(ans, inr, dcr)

        return ans