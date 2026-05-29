class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_replaced = float('inf')
        for num in nums:
            replaced = 0

            while num != 0:
                num, mod = num //10, num % 10
                replaced += mod

            if min_replaced > replaced:
                min_replaced = replaced

        return min_replaced