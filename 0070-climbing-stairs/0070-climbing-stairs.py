class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * 3
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[2] = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], dp[2]

        return dp[-1]