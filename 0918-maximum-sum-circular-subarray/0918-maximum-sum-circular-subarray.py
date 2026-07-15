class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalmax = globalmin = nums[0]
        curmax = curmin = total = 0

        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            total += n
            globalmax = max(globalmax, curmax)
            globalmin = min(globalmin, curmin)
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax
