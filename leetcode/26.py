#Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        v = 0
        if len(nums) == 1:
            return 1
        while True:
            if nums[i] == nums[i-1]:
                nums.append("_")
                nums.pop(i)
                i = i - 1
            if nums[i] == "_":
                v = i
                break
            if i == len(nums)-1:
                v = i + 1
                break
            i = i + 1
        return v