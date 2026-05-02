class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def calc(n):
            total = 0
            while n != 0:
                n, mod = n // 10, n % 10
                total += mod * mod
            return total

        while True:
            n = calc(n)

            if n in visited:
                return False
            elif n == 1:
                return True

            visited.add(n)

        return