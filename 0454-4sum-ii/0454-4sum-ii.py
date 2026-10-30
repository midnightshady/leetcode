class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        i = 0
        j = 0
        
        freqMap= {}
        count = 0
        while i < len(nums1):
            j = 0
            while j < len(nums2):
                temp = nums1[i] + nums2[j] 
                freqMap[temp] = freqMap.get(temp, 0) + 1
                j += 1
            i += 1
            
        i = 0
        
        while  i < len(nums3):
            j = 0
            while j < len(nums4):
                temp =  nums3[i] + nums4[j]
                needed = -temp
                j += 1
                
                count += freqMap.get(needed, 0)
            i += 1
        return count