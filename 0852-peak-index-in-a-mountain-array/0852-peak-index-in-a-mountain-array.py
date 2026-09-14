from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]:
                start =  mid + 1
            elif arr[mid] < arr[mid - 1]:
                end = mid - 1
            else:
                return mid