from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # First occurrence
        start = 0
        end = len(nums) - 1
        first = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                first = mid
                end = mid - 1       # left side mein search

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1


        # Last occurrence
        start = 0
        end = len(nums) - 1
        last = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                last = mid
                start = mid + 1     # right side mein search

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return [first, last]
