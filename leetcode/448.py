#Find All Numbers Disappeared in a Array
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        set1 = set(nums)
        for i in range(1,len(nums)+1,1):
            if i not in set1:
                result.append(i)
        return result