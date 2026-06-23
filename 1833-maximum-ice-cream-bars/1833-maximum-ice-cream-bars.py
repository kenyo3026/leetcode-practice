class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        max_bars = 0
        cost_so_far = 0
        for cost in costs:
            cost_so_far += cost
            if cost_so_far > coins:
                break
            max_bars += 1

        return max_bars