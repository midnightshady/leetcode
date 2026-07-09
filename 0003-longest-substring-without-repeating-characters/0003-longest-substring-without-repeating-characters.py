class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = res = left = total = 0
        freq = {}

        for right in range(len(s)):
        # freq[s[right]] = freq.get(right, 0) + 1
            freq[s[right]] = freq.get(s[right], 0) + 1
            total += 1
        
            while freq[s[right]] > 1:
                f = s[left] 
                freq[f] -= 1
                left += 1
                total -= 1
            
                if freq[f] == 0:
                    del freq[f]
            res = max(res, total)
        return res
            