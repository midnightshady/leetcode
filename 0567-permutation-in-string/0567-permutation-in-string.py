class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        target = {}
        window = {}
        left = 0

        for ch in s1:
            target[ch] = target.get(ch, 0) + 1
        
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]
                 
                left += 1

            if window == target:
                return True 
        return False