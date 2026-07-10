class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = right = mx = res = total = win = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            mx = max(mx, freq[s[right]])
            while (right - left + 1) - mx > k:
                f = s[left]
                freq[f] -= 1
                left += 1
                if freq[f] == 0:
                    del freq[f]
            total = right - left + 1
            res = max(res, total)
        return res