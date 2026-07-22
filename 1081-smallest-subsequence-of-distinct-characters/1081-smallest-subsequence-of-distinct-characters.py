class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {}
        for i in range(len(s)):
            char = s[i]
            last_index[char] = i
        
        stack = []
        visited = set()

        for i in range(len(s)):
            char = s[i]
            if char in visited :
                continue
            while (stack and stack[-1] > char and last_index[stack[-1]] > i):
                visited.remove(stack.pop())
            
            stack.append(char)
            visited.add(char)
        return "".join(stack)