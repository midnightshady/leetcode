class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)

        n = len(nums)
        half = (n + 1) // 2

        ans = 0

        for i, num in enumerate(nums):
            if i < half:
                ans += num * num
            else:
                ans -= num * num

        return ans

        