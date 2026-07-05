class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        Sum = 0

        for i in range(k):
            Sum += nums[i]
        avg = Sum / float(k)

        l = 0
        r = k - 1

        while r < len(nums) - 1:
            Sum = Sum - nums[l] + nums[r + 1]
            new_avg = Sum / float(k)
            avg = max(avg, new_avg)
            l += 1
            r += 1
        return avg        
            