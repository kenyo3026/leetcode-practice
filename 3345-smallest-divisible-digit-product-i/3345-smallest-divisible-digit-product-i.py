class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def calc_digit_product(n):
            product = 1
            while n != 0:
                div, mod = n // 10, n % 10
                n = div
                product *= mod
            return product

        while True:
            if calc_digit_product(n) % t == 0:
                return n
            n += 1
        return