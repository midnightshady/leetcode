class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = float("-inf")
        second_largest = float("-inf")
        
        for i in nums:
            if (largest < i):
                second_largest = largest
                largest = i
                
            elif(second_largest < i):
               second_largest = i
        return (largest - 1) * (second_largest - 1)
            
            
        