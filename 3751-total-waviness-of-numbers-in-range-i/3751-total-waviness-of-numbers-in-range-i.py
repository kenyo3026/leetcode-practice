class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            digits = [int(d) for d in str(x)]
            if len(digits) < 3:
                return 0
            count = 0
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                    count += 1  # peak
                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                    count += 1  # valley
            return count

        return sum(waviness(x) for x in range(num1, num2 + 1))