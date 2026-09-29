class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')':
            return False

        memo = set()

        def dfs(r, c, balance):

            # current cell process karo
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # invalid
            if balance < 0:
                return False

            # last cell
            if r == m - 1 and c == n - 1:
                return balance == 0

            state = (r, c, balance)

            if state in memo:
                return False

            memo.add(state)

            # down
            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    return True

            # right
            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    return True

            return False

        return dfs(0, 0, 0)