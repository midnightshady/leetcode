class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        y = len(needle)
        for x in range(len(haystack)):
            if needle == haystack[x : x+y]:
                return x
        return -1