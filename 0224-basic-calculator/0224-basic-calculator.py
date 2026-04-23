class Solution:
    def calculate(self, s: str) -> int:

        def _calc(s: str, idx: int = 0):
            n = len(s)
            sign, num = 1, 0
            total = 0

            # for i in range(idx, n):
            while idx < n:
                token = s[idx]

                if token == ' ':
                    idx += 1
                    continue

                elif token.isdigit():
                    num = num * 10 + int(token)

                elif token == '+':
                    total += sign * num
                    sign, num = 1, 0

                elif token == '-':
                    total += sign * num
                    sign, num = -1, 0

                elif token == '(':
                    num, idx = _calc(s, idx + 1)
                    # idx -= 1

                elif token == ')':
                    total += sign * num
                    return total, idx

                idx += 1

            total += sign * num
            return total, n

        total, _ = _calc(s)
        return total