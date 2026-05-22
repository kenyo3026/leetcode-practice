class Solution:
    def rotatedDigits(self, n: int) -> int:
        bad_mask = (1 << 3) | (1 << 4) | (1 << 7)
        good_mask = (1 << 2) | (1 << 5) | (1 << 6) | (1 << 9)

        good_found = 0
        for num in range(1, n+1):
            mask = 0
            while num != 0:
                mask |= (1 << num % 10)
                num //= 10

            if not (mask & bad_mask) and (mask & good_mask):
                good_found += 1

        return good_found