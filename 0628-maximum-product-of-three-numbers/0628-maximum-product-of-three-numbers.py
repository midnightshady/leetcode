class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum1 = nums[-1] * nums[-2] * nums[-3]
        sum2 = nums[0] * nums[1] * nums[-1]

        return max(sum1, sum2)