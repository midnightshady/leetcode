class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = []
        curr = 0
        for i in nums:
            curr += i
            sm.append(curr)
        Left = 0
        temp = sm[-1]
        
        for i in range(len(nums)):
            Right = temp - sm[i]
            if Left == Right:
                return i
            Left = sm[i]
        return -1