class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
      low = 1
      high = max(nums)
      ans = float('inf')
      
      while low <= high:
            temp = 0
            mid = (low + high) // 2
            for i in nums:
                temp += (i + mid - 1) // mid

            if temp <= threshold:
                ans = min(mid, ans)
                high = mid - 1
            else:
                low = mid + 1
      return ans