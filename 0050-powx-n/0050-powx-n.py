class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = n
        def count(x, n):
            
            if n == 0:
                return 1
        
            half = count(x, n // 2)
            
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        if temp < 0:
            return 1 / (count(x, abs(n)))
        return count(x, n)