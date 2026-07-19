class Solution(object):
    def majorityElement(self, nums):
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for key, value in seen.items():
            if value > len(nums) / 2 :
                return key 
        