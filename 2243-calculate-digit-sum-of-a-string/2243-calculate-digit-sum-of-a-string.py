class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            digit_sums = ['']
            for i in range(0, len(s)):
                if i % k == 0:
                    digit_sums[-1] = str(digit_sums[-1])
                    digit_sums.append(0)
                digit_sums[-1] += int(s[i])

            digit_sums[-1] = str(digit_sums[-1])
            s = ''.join(digit_sums)

        return s