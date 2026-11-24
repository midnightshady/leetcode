import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        # Upper bound for lcm(arr) * gcd(arr) to stop early if product grows too large
        max_possible = math.lcm(*nums) * max(nums)
        
        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1
            
            for j in range(i, n):
                prod *= nums[j]
                if prod > max_possible:
                    break
                    
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
