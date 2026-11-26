
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        moves = 0

        while stones > 0 and n >= stones:
            n -= stones
            stones -= 1
            moves += 1

        return moves % 2 == 1
