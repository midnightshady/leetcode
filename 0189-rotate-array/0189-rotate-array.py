from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or not nums:
            return 
        nums.reverse()
        k = k % len(nums)
        left = k 
        right = len(nums) - 1
        
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            right -= 1
            left += 1
        left = 0
        right = k  - 1
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            right -= 1
            left += 1
        return 