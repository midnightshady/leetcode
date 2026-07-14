class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        temp ={}
        res = float("inf")
        ans = ""

        for c in t:
            temp[c] = temp.get(c, 0) + 1

        count = len(t)
        left = 0

        for right in range(len(s)):
            c = s[right]
            
            if c in temp :
                if temp[c] > 0:
                    count -= 1
                temp[c] -= 1
            
            while count == 0:
                if right - left + 1 < res:
                    res = right - left + 1
                    ans = s[left : right + 1]
                left_char = s[left]
                
                if left_char in temp:
                    temp[left_char] += 1
                    if temp[left_char] > 0:
                        count += 1
                left += 1
        return ans   