class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftQnmarkcount = leftKnownsum = rightQnmarkcount = rightKnownsum = 0
        for i in range(len(num)):
            if num[i] == "?":
                if i < n // 2:
                    leftQnmarkcount += 1
                else:
                    rightQnmarkcount += 1
            else:
                if i < n // 2:
                    leftKnownsum += int(num[i])
                else:
                    rightKnownsum += int(num[i])
        totalQnmarkcount = leftQnmarkcount + rightQnmarkcount
        
        if totalQnmarkcount % 2 == 1:
            return True
        
        LEFT = 2 * leftKnownsum + 9 * leftQnmarkcount
        RIGHT = 2 * rightKnownsum + 9 * rightQnmarkcount
        
        if LEFT == RIGHT:
            return False
        return True