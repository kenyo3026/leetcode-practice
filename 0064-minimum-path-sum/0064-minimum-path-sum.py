class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):

                min_adds = []
                if 0 <= i-1 < n:
                    min_adds.append(grid[i-1][j])
                if 0 <= j-1 < m:
                    min_adds.append(grid[i][j-1])

                grid[i][j] += min(min_adds) if min_adds else 0

        return grid[-1][-1]
        