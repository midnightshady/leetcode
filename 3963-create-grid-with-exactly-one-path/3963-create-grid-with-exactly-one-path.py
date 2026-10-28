
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        for i in range(m):
            row = ['#'] * n
            row[n - 1] = '.'
            grid.append(''.join(row))

        grid[0] = '.' * n

        return grid
