class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return sum(cost)

        cost.sort()

        total_cost = 0
        next_free = n - 3
        for i in range(n-1, -1, -1):
            if i == next_free:
                next_free -= 3
            else:
                total_cost += cost[i]

        return total_cost

