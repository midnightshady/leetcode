class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = 1
        stack = []
        ans = ""
        for ch in range(len(s) - 1, -1, -1):
            char = s[ch]
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, cnt])
            if stack and stack[-1][1] == k:
                stack.pop()

        result = ""
        for ch, cnt in stack:
            result += ch * cnt
        return result[::-1]