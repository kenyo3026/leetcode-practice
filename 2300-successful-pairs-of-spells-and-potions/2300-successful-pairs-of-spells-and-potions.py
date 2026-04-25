class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)

        def bs(multiplier, target):
            left, right = 0, m

            while left < right:
                mid = (left + right) // 2
                val = potions[mid] * multiplier

                if val >= target:
                    right = mid
                else:
                    left = mid + 1

            return m - left

        return [bs(spell, success) for spell in spells]