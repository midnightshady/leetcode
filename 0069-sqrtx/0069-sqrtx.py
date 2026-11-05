class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        
        while low <= high:
            mid = (low + high) // 2
            root = mid * mid
            if root == x:
                return mid
            elif root > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans