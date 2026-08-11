from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        i = 1
        while(i != len(ratings)):
            if (ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]):
                candies[i] = candies[i - 1] + 1
            i += 1
        i = len(ratings) - 1
        sum = 0
        while (i > 0):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
            sum += candies[i]
            i -= 1
        sum += candies[i]
        return sum
                
soln = Solution()
print(soln.candy([1,0,2]))