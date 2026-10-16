class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        if len(nums) < k:
            return - 1
            
        low = max(nums)
        high = sum(nums) 
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            temp = 0
            subArray = 1
            for i in nums:
                if temp + i <= mid:
                    temp += i
                
                else:
                    subArray += 1
                    temp = i
            if subArray <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            