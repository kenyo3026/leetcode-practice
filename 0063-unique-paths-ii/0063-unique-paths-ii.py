class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacle, space = 1, 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == obstacle:
                    dp[i][j] = 0
                else:
                    dp[i][j] += (dp[i][j-1] + dp[i-1][j])

        return dp[-1][-1]