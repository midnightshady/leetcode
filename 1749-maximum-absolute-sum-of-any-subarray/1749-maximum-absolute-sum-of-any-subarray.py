class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = float('-inf')
        min_sum = float('inf')
        
        curr_min = 0
        curr_max = 0
        
        for n in nums:
            curr_max += n
            curr_min += n
            
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
            
            if curr_max < 0:
                curr_max = 0
            
            if curr_min > 0:
                curr_min = 0
        return max(max_sum, abs(min_sum))