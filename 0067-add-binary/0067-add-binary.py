class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai, bi = len(a) - 1, len(b) - 1
        added = []
        carry = 0

        while ai >= 0 or bi >= 0 or carry:

            if ai >= 0:
                carry += int(a[ai])
                ai -= 1

            if bi >= 0:
                carry += int(b[bi])
                bi -= 1

            added.append(str(carry % 2))
            carry //= 2

        return ''.join(added[::-1])