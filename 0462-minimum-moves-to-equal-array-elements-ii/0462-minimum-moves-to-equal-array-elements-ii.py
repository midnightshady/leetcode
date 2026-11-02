from typing import List
class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        temp = sorted(nums)
        median = len(temp) // 2
        count = 0

        for x in range(len(nums)):
            count += abs(temp[median] - nums[x])

        return count