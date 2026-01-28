class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_1 = 0

        while n != 0:
            num_of_1 += 1
            n = n & (n - 1)

        return num_of_1