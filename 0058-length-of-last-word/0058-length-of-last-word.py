class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            while(i >= 0 and s[i] == " "):
                i -= 1
            if i < 0:
                break
            end = i
            while (i >= 0 and s[i] != " "):
                i -= 1
            start = i 
            return end - start