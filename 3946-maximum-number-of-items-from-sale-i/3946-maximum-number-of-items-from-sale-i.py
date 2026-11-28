class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        buy_1_get_x = [1] * n
        for i, (fac_i, _) in enumerate(items):
            for j, (fac_j, _) in enumerate(items):
                if i != j and fac_j % fac_i == 0:
                    buy_1_get_x[i] += 1

        dp = [0] * (budget + 1)
        for i, (_, price) in enumerate(items):
            got_x = buy_1_get_x[i]

            for b in range(budget, price-1, -1):
                dp[b] = max(dp[b], dp[b-price]+got_x)

        min_price = min(price for _, price in items)
        ans = 0
        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // min_price)
        return ans