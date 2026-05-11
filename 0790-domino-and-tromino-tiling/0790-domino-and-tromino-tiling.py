class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        full = [0] * (n + 1)
        part = [0] * (n + 1)

        full[0], full[1] = 1, 1
        for i in range(2, n+1):
            full[i] = full[i-1] + full[i-2] + 2 * part[i-1]
            part[i] = full[i-2] + part[i-1]

        return full[-1]