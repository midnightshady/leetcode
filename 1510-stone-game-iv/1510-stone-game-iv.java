class Solution {
    Boolean dp[];

    private boolean solve(int n) {
        // base case 
        if (n == 0) {
            return false; // whoever sees this fails so they lose
        }

        if (dp[n] != null) {
            return dp[n];
        }

        for (int i = 1; i * i <= n; i++) {
            // if bob returns false means he lost 
            // means alice wins 
            if (solve(n - (i * i)) == false) {
                return dp[n] = true;
            }
        }

        // bob wins as we didnt find bob losing 
        return dp[n] = false;

    }

    public boolean winnerSquareGame(int n) {
        // alice plays first and can take from 1^2 to n^2 if piles are there 
        dp = new Boolean[n + 1];
        return solve(n);
    }
}