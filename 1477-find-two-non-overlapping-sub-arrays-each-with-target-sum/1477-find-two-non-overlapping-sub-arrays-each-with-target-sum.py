class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        n = len(arr)
        x = 0
        current_sm = 0
        best = [float('inf')] * (n + 1)
        ans = float('inf')
        
        for y in range(n):
            current_sm += arr[y]
            
            while current_sm > target:
                current_sm -= arr[x]
                x += 1
            
            if current_sm == target:
                length = y - x + 1
                
                if best[x] != float('inf'):
                    ans = min(ans, length + best[x])
                    
                best[y + 1] = min(best[y], length)
            else:
                best[y + 1] = best[y]
        
        return -1 if ans == float('inf') else ans