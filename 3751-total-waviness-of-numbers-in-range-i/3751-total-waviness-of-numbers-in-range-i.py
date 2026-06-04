class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def waviness(num):
            digits = str(num)
            n = len(digits)

            count = 0
            for i in range(1, n-1):
                if (digits[i-1] < digits[i] and digits[i] > digits[i+1]) or \
                    (digits[i-1] > digits[i] and digits[i] < digits[i+1]):
                    count += 1

            return count

        return sum(waviness(num) for num in range(num1, num2+1))