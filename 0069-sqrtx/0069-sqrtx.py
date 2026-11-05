class Solution:
    def mySqrt(self, x: int) -> int:
        sqr = x

        def sqrt(low, high, ans):
            if low > high:
                return ans

            mid = (low + high) // 2
            root = mid * mid

            if root == sqr:
                return mid

            elif root > sqr:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

            return sqrt(low, high, ans)

        return sqrt(0, x, 0)