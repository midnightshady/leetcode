class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        best_pos = -1
        best_char = -1

        # Try to match target from left to right
        for i in range(len(target)):

            # Can we put a character GREATER than target[i] here?
            for c in range(ord(target[i]) - ord('a') + 1, 26):
                if count[c] > 0:
                    best_pos = i
                    best_char = c

                    # We want the RIGHTMOST possible position,
                    # so keep going.
                    break

            # Try to use target[i] itself
            x = ord(target[i]) - ord('a')

            if count[x] == 0:
                # Can't match target anymore
                break

            count[x] -= 1

        # No permutation is greater than target
        if best_pos == -1:
            return ""

        # Recreate counts because they were modified
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Use characters of target before best_pos
        for i in range(best_pos):
            count[ord(target[i]) - ord('a')] -= 1

        # Use the character that makes it greater
        count[best_char] -= 1

        # Remaining characters should be smallest possible => sorted
        suffix = []

        for c in range(26):
            suffix.append(chr(c + ord('a')) * count[c])

        return target[:best_pos] + chr(best_char + ord('a')) + ''.join(suffix)