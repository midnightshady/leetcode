class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import fractions

        # 1. Sabse chota aur bada number nikalen
        min_num = min(nums)
        max_num = max(nums)
        
        # 2. fractions module ka gcd use karen
        return fractions.gcd(min_num, max_num)
        