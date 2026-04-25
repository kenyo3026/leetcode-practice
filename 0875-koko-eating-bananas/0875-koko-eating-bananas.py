class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def get_min_hour_needed(k):
            total = 0
            for pile in piles:
                total += (pile + k - 1) // k
            return total

        while left < right:
            mid = (left + right) // 2
            min_needed = get_min_hour_needed(mid)

            if min_needed > h:
                left = mid + 1
            else:
                right = mid

        return left