class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        dp = [0] + [float('inf')] * amount

        for i in range(amount+1):
            for coin in coins:
                if coin > i:
                    continue

                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float('inf') else -1