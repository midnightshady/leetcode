class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        # Frequency of characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # More than one odd frequency => palindrome impossible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Make frequency of first half
        halfCount = [0] * 26

        for i in range(26):
            halfCount[i] = count[i] // 2

        n = len(s)
        halfLen = n // 2

        targetHalf = target[:halfLen]

        # Try to match target's first half
        remaining = halfCount[:]
        matched = 0

        while matched < halfLen:
            x = ord(targetHalf[matched]) - ord('a')

            if remaining[x] == 0:
                break

            remaining[x] -= 1
            matched += 1

        # Build palindrome from a half
        def makePalindrome(half):
            if n % 2 == 1:
                return half + middle + half[::-1]
            else:
                return half + half[::-1]

        # If complete target half can be formed
        if matched == halfLen:

            candidate = makePalindrome(targetHalf)

            # It must be STRICTLY greater
            if candidate > target:
                return candidate

        # Find the smallest half greater than targetHalf
        # Start from the rightmost possible position

        if matched == halfLen:

            available = [0] * 26

            for i in range(halfLen - 1, -1, -1):

                x = ord(targetHalf[i]) - ord('a')
                available[x] += 1

                for c in range(x + 1, 26):

                    if available[c] > 0:

                        available[c] -= 1

                        half = targetHalf[:i]
                        half += chr(c + ord('a'))

                        for j in range(26):
                            half += chr(j + ord('a')) * available[j]

                        return makePalindrome(half)

        else:

            available = remaining[:]

            for i in range(matched, -1, -1):

                if i < matched:
                    x = ord(targetHalf[i]) - ord('a')
                    available[x] += 1

                x = ord(targetHalf[i]) - ord('a')

                for c in range(x + 1, 26):

                    if available[c] > 0:

                        available[c] -= 1

                        half = targetHalf[:i]
                        half += chr(c + ord('a'))

                        for j in range(26):
                            half += chr(j + ord('a')) * available[j]

                        return makePalindrome(half)

        return ""
        