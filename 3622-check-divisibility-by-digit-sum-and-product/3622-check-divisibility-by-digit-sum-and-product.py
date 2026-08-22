class Solution:
    def checkDivisibility(self, n: int) -> bool:

        def get_sum_and_prod(n):
            val_sum, val_prod = 0, 1
            while n != 0:
                div, mod = n // 10, n % 10
                val_sum += mod
                val_prod *= mod
                n = div
            return val_sum, val_prod

        val_sum, val_prod = get_sum_and_prod(n)
        return n % (val_sum + val_prod) == 0