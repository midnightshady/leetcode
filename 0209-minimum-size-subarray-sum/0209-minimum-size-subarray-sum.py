class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        Sum = 0
        minlength = float('inf')

        for right in range(len(nums)):
            Sum = Sum + nums[right]

            while Sum >= target:
                Sum = Sum - nums[left]
                minlength = min(minlength, right - left + 1)
                left += 1
        if minlength == float('inf'):
            return 0
        return minlength