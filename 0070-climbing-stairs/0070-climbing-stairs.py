class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = 0
        dp_1, dp_2 = 2, 1
        for i in range(3, n+1):
            dp = dp_1 + dp_2
            dp_1, dp_2 = dp, dp_1

        return dp