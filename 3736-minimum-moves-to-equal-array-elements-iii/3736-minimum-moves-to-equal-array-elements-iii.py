class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max = max(nums)
        count = 0
        for x in nums:
            temp = Max - x
            count += temp
        return count