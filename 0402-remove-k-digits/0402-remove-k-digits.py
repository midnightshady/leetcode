class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = 0
        for x in num:
            while(stack and stack[-1] > x and count != k):
                stack.pop()
                count += 1
            stack.append(x)
        while count != k:
            stack.pop()
            count += 1
        result = "".join(stack).lstrip("0")
        if result == "":
            return "0"
        return result
        