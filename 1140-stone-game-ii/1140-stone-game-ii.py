class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = piles[i] + piles[i+1] + ...
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, M):
            # Remaining stones can all be taken
            if i >= n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # X can be from 1 to 2*M
            for X in range(1, 2 * M + 1):

                # Opponent gets to play from i+X
                opponent = dfs(i + X, max(M, X))

                # Total remaining - opponent's maximum
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dfs(0, 1)