class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        digits = []
        for _ in range(num):
            choice = min(9, sum)
            digits.append(str(choice))
            sum -= choice

        return "".join(digits)