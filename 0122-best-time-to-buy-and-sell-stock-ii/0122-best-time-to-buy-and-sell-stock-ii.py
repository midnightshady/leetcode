class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        i = 0
        j = 0
        profit = 0
        
        while i < len(nums) - 1 :
            j = i + 1
            if nums[j] - nums[i] > 0:
                profit += nums[j] - nums[i]
            i += 1
        return profit