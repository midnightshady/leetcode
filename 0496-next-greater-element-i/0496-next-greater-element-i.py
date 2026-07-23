class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        ans = []
        for i in range(len(nums2) -1, -1, -1):
            if not stack :
                dic[nums2[i]] = -1
            if stack and nums2[i] < stack[-1]:
                dic[nums2[i]] = stack[-1]
            while (stack and nums2[i] > stack[-1]):
                stack.pop()
                if not stack:
                    dic[nums2[i]] = -1
                else:
                    dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in nums1:
            ans.append(dic[i])
        return ans