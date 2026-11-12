#Seach Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = target
        for i in range(0,len(nums),1):
            if nums[i] == a:
                return int(i)
            elif a < nums[i]:
                return int(i)
            elif a > max(nums):
                return int(len(nums))
        return False

        