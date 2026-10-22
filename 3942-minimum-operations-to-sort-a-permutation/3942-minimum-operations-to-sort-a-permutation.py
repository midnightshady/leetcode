
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0

        k = nums[0]

        # Check whether nums is a cyclic ascending sequence
        if all(nums[i] == (k + i) % n for i in range(n)):
            return min((n - k) % n, k + 2)

        # Check whether nums is a cyclic descending sequence
        if all(nums[i] == (k - i) % n for i in range(n)):
            x = (k + 1) % n
            return 1 + min(x, (n - x) % n)

        return -1
