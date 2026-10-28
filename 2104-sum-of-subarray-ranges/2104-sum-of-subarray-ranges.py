class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        sum = 0
        
        for i in range(len(nums)):
            largest = nums[i]
            smallest = nums[i]
            
            for j in range(i + 1, len(nums)):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                sum += largest - smallest
        return sum