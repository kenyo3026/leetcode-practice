class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def one_shift(grid):
            last_col_nums = [grid[m-1][n-1]] * m
            for i in range(1, m):
                last_col_nums[i] = grid[i-1][n-1]

            for i in range(m-1, -1, -1):
                for j in range(n-1, 0, -1):
                    grid[i][j] = grid[i][j-1]

            for i in range(m):
                grid[i][0] = last_col_nums[i]

        for _ in range(k):
            one_shift(grid)

        return grid