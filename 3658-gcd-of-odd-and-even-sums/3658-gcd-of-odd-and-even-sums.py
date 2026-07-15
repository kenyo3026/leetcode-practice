class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sum_odd, sum_even = 0, 0
        # for i in range(1, n*2+1, 2):
        #     sum_odd += i
        #     sum_even += i+1

        # smaller = min(sum_odd, sum_even)
        # for i in range(smaller, 0, -1):
        #     if sum_odd % i == 0 and sum_even % i == 0:
        #         return i
        # return 1
        return n