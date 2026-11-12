#622/681 testcases
#runtime error
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        peaks = []
        for query in queries:
            if query[0]==1:
                l = query[1]
                r = query[2]

                count = 0
                for i in range(l+1,r,1):
                    if nums[i] > nums[i-1] and nums[i]>nums[i+1]:
                        count+= 1

                peaks.append(count)

            else:
                index = query[1]
                val = query[2]

                nums[index] = val
        return peaks