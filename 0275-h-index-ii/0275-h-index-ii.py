class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        start = 0
        end = n - 1
        ans = 0
        
        while start <= end:
            mid = start + (end - start) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                end = mid - 1
            else:
                start = mid + 1
        return ans