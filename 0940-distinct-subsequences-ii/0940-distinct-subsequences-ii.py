class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [1]
        last = {}

        for i, ch in enumerate(s, 1):
            curr = (2 * dp[-1]) % MOD

            if ch in last:
                curr -= dp[last[ch] - 1]
                curr %= MOD

            dp.append(curr)
            last[ch] = i

        return (dp[-1] - 1) % MOD