class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {}
        n = len(s)
        
        i = 0
        j = 0 
        count = 0
        freq[s[j]] = 1
        
        while j <  n:
            if 'a' in freq and 'b' in freq and 'c' in freq:
                # count += 1
                count += n - j
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i += 1
            else:
                j += 1
                if j < n:
                    freq[s[j]] = freq.get(s[j], 0) + 1
        return count