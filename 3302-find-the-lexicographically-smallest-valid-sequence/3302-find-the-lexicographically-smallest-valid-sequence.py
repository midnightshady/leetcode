class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:

        n = len(word1)
        m = len(word2)

        rightHandSideMatchLength = [0] * (n + 1)

        rightMatched = 0
        i = n - 1
        j = m - 1

        while i >= 0:

            if j >= 0 and word1[i] == word2[j]:
                rightMatched += 1
                j -= 1

            rightHandSideMatchLength[i] = rightMatched
            i -= 1

        seq = []

        changePower = True

        i = 0
        j = 0

        while i < n and j < m:

            if word1[i] == word2[j]:
                seq.append(i)
                j += 1

            elif changePower and rightHandSideMatchLength[i + 1] >= m - j - 1:
                seq.append(i)
                j += 1
                changePower = False

            i += 1

        if j == m:
            return seq

        return []