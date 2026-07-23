class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):
            char1 = nums1[i]
            found = False
            for j in range(len(nums2)):
                if char1 == nums2[j]:
                    j += 1
                    while j < len(nums2):
                        if char1 < nums2[j]:
                            ans.append(nums2[j])
                            found = True
                            break
                        j += 1
                    if not found :
                        ans.append(-1)
        return ans