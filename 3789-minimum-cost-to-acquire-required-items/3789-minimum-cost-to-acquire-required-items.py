class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        low, high = min(need1, need2), max(need1, need2)

        eq1 = (need1 * cost1) + (need2 * cost2)
        eq2 = (low * costBoth) + ((need1 - low) * cost1) + ((need2 - low) * cost2)
        eq3 = (high * costBoth)

        return min(eq1, eq2, eq3)