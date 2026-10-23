class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        if nums == list(range(len(nums))):
            return 0

        k = -1

        for i in range(len(nums)):
            if nums[i] != i:
                if k == -1:
                    k = nums[i]
                else:
                    k &= nums[i]

        return k
