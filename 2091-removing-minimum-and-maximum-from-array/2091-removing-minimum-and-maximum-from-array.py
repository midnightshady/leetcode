class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_val = min(nums)
        max_val = max(nums)

        min_idx = nums.index(min_val)
        max_idx = nums.index(max_val)

        # min aur max ko left/right order mein rakho
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Case 1: dono front se
        case1 = right + 1

        # Case 2: dono back se
        case2 = n - left

        # Case 3: left wala front se, right wala back se
        case3 = (left + 1) + (n - right)

        return min(case1, case2, case3)