class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        l = 0
        count = 0
        result = ""

        for r in range(len(s)):

            if s[r] == '1':
                count += 1

            while count == k:

                # Current valid window
                candidate = s[l:r + 1]

                # Best answer update
                if result == "" or len(candidate) < len(result):
                    result = candidate

                elif len(candidate) == len(result) and candidate < result:
                    result = candidate

                # Shrink from left
                if s[l] == '1':
                    count -= 1

                l += 1

        return result