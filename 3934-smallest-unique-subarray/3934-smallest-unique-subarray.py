
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        B1, M1 = 911382323, 1_000_000_007
        B2, M2 = 972663749, 1_000_000_009

        def has_unique(length):
            p1 = pow(B1, length - 1, M1)
            p2 = pow(B2, length - 1, M2)

            h1 = h2 = 0

            # Calculate first window hash
            for x in nums[:length]:
                h1 = (h1 * B1 + x) % M1
                h2 = (h2 * B2 + x) % M2

            freq = {(h1, h2): 1}

            # Slide the window
            for right in range(length, n):
                left = right - length

                h1 = ((h1 - nums[left] * p1) * B1
                      + nums[right]) % M1

                h2 = ((h2 - nums[left] * p2) * B2
                      + nums[right]) % M2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        # Binary Search
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if has_unique(mid):
                high = mid
            else:
                low = mid + 1

        return low
