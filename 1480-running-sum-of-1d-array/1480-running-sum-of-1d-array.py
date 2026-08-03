class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = 0
        for i in range(len(nums)):
            sm = sm + nums[i]
            nums[i] = sm
        return nums