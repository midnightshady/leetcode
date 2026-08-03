from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = 0
        for i in range(len(nums)):
            sm = sm + nums[0]
            nums.pop(0)
            nums.append(sm)
        return nums