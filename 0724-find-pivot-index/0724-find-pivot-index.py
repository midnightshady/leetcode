class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Left = 0
        temp = sum(nums)
        
        for i in range(len(nums)):
            Right = temp - nums[i] - Left
            if Left == Right:
                return i
            Left += nums[i]
        return -1