class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        current = 0
        nxt = current + 1
        result = 0
        while current < len(s):
            if current == len(s) - 1:
                temp = roman[s[current]]
                current += 1
            elif nxt < len(s) and roman[s[current]] < roman[s[nxt]]:
                temp = roman[s[nxt]] - roman[s[current]]
                current = nxt + 1
            else:
                temp = roman[s[current]]
                current += 1
            result += temp
            nxt = current + 1
        return result
