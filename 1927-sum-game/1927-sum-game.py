class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        sum_diff = 0
        cnt_diff = 0
        for i in range(1, n // 2 + 1):

            if num[i-1] == "?":
                cnt_diff += 1
            else:
                sum_diff += int(num[i-1])

            if num[-i] == "?":
                cnt_diff -= 1
            else:
                sum_diff -= int(num[-i])

        return sum_diff != -9 * (cnt_diff) / 2