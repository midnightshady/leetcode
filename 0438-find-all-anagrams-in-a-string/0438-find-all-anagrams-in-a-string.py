class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        target = {}
        window = {}
        left = 0
        res = []

        for ch in p:
            target[ch] = target.get(ch, 0) + 1
        
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                left_char = s[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]
                 
                left += 1

            if window == target:
                res.append(left)
        return res