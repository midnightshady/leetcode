class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        op = " ".join(words)
        return op