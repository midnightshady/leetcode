class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            product = 1
            temp = n
            while temp:
                digit = temp % 10
                product *= digit
                temp //= 10
            if product % t == 0:
                return n
            else:
                n += 1