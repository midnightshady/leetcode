class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        def square(low, high, ans):
            if low > high:
                return False
            
            mid = (low + high) // 2
            root = mid * mid
            
            if root == num:
                return True
            elif root > num:
                high = mid - 1
            else:
                low = mid + 1
            
            return square(low, high, ans)
        return square(0, num, 0)