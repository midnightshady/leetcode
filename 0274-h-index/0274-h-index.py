class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * (max(citations) + 1)
        i = 0
        while(i < len(citations)):
            count[citations[i]] += 1
            i += 1
        
        i = 0
        for num in range(len(count)):
            while count[num] > 0:
                citations[i] = num
                i += 1
                count[num] -= 1
        n = len(citations)
        for i in range(len(citations)):
            if citations[i] >= n - i:
                return n - i
        return 0