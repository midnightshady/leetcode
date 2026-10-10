
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(d - mid, 0) for d in diffs)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        used = sum(max(d - level, 0) for d in diffs)
        remaining = k - used

        result = sum(min(d, level) ** 2 for d in diffs)

        if level > 0:
            result -= remaining * (2 * level - 1)

        return result
