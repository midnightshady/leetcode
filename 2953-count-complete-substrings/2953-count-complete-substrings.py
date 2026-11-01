
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        start = 0

        for i in range(1, n + 1):
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                segment = word[start:i]
                length = len(segment)

                for unique in range(1, 27):
                    window_size = unique * k
                    if window_size > length:
                        break

                    freq = [0] * 26
                    good = 0

                    for j in range(window_size):
                        idx = ord(segment[j]) - ord('a')
                        freq[idx] += 1

                    if sum(x > 0 and x == k for x in freq) == unique:
                        ans += 1

                    for right in range(window_size, length):
                        left_idx = ord(segment[right - window_size]) - ord('a')
                        right_idx = ord(segment[right]) - ord('a')

                        freq[left_idx] -= 1
                        freq[right_idx] += 1

                        if sum(x > 0 and x == k for x in freq) == unique:
                            ans += 1

                start = i

        return ans
