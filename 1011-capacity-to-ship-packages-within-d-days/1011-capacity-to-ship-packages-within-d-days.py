class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = right
        while left <= right :
            mid = (left + right) // 2
            currentLoad = 0
            daysCount = 1
            
            for weight in weights:
                if currentLoad + weight <= mid:
                    currentLoad += weight
                else:
                    currentLoad = weight
                    daysCount +=1
            
            if daysCount <= days:
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans 