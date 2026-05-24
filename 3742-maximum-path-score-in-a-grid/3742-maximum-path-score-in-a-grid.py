from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        NEG = -10**18

        # dp[i][j] = dict: remain -> best score
        dp = [[{} for _ in range(n)] for _ in range(m)]

        def add(dp_cell, remain, score):
            if remain < 0:
                return
            if remain not in dp_cell or dp_cell[remain] < score:
                dp_cell[remain] = score

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cost = 1 if val > 0 else 0

                if i == 0 and j == 0:
                    add(dp[i][j], k, 0)
                    continue

                cur = dp[i][j]
                if i > 0:
                    for r, s in dp[i-1][j].items():
                        nr = r - cost
                        if nr >= 0:
                            add(cur, nr, s + val)
                if j > 0:
                    for r, s in dp[i][j-1].items():
                        nr = r - cost
                        if nr >= 0:
                            add(cur, nr, s + val)

        res = -1
        for r, s in dp[m-1][n-1].items():
            res = max(res, s)

        return res