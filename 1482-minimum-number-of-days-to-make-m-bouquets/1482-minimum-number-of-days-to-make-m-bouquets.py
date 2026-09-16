class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        flowers = m * k
        if flowers > len(bloomDay):
            return -1
            
        start = 0
        end = max(bloomDay)
        
        while start < end :
            mid = (start + end) // 2
            consecutive = 0
            bouquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    consecutive += 1
                    
                    if consecutive == k:
                        bouquet += 1
                        consecutive = 0
                else:
                    consecutive = 0
            
            if bouquet >= m:
                end = mid
            else:
                start = mid + 1
        return start