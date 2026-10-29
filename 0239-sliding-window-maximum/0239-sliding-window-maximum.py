from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # indices store honge
        result = []

        for j in range(len(nums)):

            # 1. Window se bahar wale indices remove karo
            if dq and dq[0] <= j - k:
                dq.popleft()

            # 2. Chhote ya equal elements ke indices remove karo
            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()

            # 3. Current index add karo
            dq.append(j)

            # 4. Jab complete window ban jaaye, maximum store karo
            if j >= k - 1:
                result.append(nums[dq[0]])

        return result


soln = Solution()
print(soln.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))