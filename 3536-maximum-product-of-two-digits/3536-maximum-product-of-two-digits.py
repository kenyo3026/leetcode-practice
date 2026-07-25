class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        max_1, max_2 = float('-inf'), float('-inf')
        while n != 0:
            div, mod = n // 10, n % 10
            n = div
            digits.append(mod)

            if mod > max_1:
                max_2 = max_1
                max_1 = mod
            elif mod > max_2:
                max_2 = mod

        return max_1 * max_2
