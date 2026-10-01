class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in closeToOpen:
                if result and result[-1] == closeToOpen[ch]:
                    result.pop()
                else:
                    return False
            else:
                result.append(ch)
        return True if not result else False