class Solution(object):
    def decodeString(self, s):
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                string = []
                while stack[-1] != "[":
                    string.append(stack.pop())
                stack.pop()
                string.reverse()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                dig = int("".join(num))

                stack.extend(string * dig)

        result = []

        while stack:
            result.append(stack.pop())
        result.reverse()
        result = str("".join(result))
        return result 

            
