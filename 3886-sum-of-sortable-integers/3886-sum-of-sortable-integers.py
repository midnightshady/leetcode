class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            previous_max = float("-inf")
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                m = len(block)

                # Count descents in the circular block
                descents = 0

                for i in range(m):
                    if block[i] > block[(i + 1) % m]:
                        descents += 1

                # More than one descent means it cannot be sorted
                # using a cyclic rotation
                if descents > 1:
                    valid = False
                    break

                # Blocks must also be in sorted order relative
                # to each other
                block_min = min(block)
                block_max = max(block)

                if previous_max > block_min:
                    valid = False
                    break

                previous_max = block_max

            if valid:
                ans += k

        return ans
