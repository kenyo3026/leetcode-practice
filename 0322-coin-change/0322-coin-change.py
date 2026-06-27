class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        dp = [0] + [float('inf')] * amount

        for i in range(amount):
            for coin in coins:
                if i + coin <= amount:
                    coin_change = i + coin
                    dp[coin_change] = min(dp[coin_change], dp[i] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1