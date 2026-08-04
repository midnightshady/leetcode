class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self. prefixsum = []
        curr = 0
        for x in nums:
            curr += x
            self. prefixsum. append(curr)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        Rightsum = self. prefixsum[right]
        Leftsum = self. prefixsum[left - 1] if left > 0 else 0
        
        return Rightsum - Leftsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)