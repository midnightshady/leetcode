from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        count = [0] * k

        for i in nums:
            new_count = [0] * k

            # Previous subarrays ko current element se extend karo
            for r in range(k):
                if count[r] != 0:
                    new_r = (r * i) % k
                    new_count[new_r] += count[r]

            # Single element subarray [i]
            new_count[i % k] += 1

            # Current ending subarrays ko overall answer mein add karo
            for r in range(k):
                ans[r] += new_count[r]

            # Ab ye current state hai
            count = new_count

        return ans