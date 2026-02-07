class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1

        for j in range(1, m):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                dp[i][j] += (dp[i-1][j] + dp[i][j-1])

        return dp[-1][-1]