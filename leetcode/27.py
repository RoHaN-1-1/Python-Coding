#Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        while True:
            if val in nums:
                nums.remove(val)
            else:
                return k
        