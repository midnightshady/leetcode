from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        st = set(nums)
        mn = min(nums)
        mx = max(nums)
        
        return [x for x in (range(mn + 1, mx)) if x not in st]
soln = Solution()
print(soln.findMissingElements([1, 4, 2, 5]))