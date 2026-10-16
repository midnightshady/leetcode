class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        import math
        if hour <= (len(dist)) - 1:
            return -1
            
        low = 1
        high = 10 ** 7
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            total = 0
            
            for i in range(len(dist) - 1):
                total += math.ceil(dist[i] / mid)
            total += dist[-1] / mid
            if total <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans