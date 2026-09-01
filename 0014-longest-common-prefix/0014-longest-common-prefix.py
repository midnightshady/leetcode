class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == "":
            return null
        result = ""
        mm = min(len(s) for s in strs)
        
        for i in range(mm):
            current = strs[0][i]
            for j in range(len(strs)):
                if current != strs[j][i]:
                    return result
                current = strs[j][i]
            result += current
        return result