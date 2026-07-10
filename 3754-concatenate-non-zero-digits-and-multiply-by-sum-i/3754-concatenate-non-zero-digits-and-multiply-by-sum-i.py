class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n_wo_zero = 0
        n_wo_zero_sum = 0
        place = 1

        while n != 0:
            div, mod = n // 10, n % 10
            if mod != 0:
                n_wo_zero = n_wo_zero + mod * place
                n_wo_zero_sum += mod
                place *= 10
            n = div

        return n_wo_zero * n_wo_zero_sum