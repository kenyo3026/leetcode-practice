class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return True

        for i in range(1, n):
            if s[i] == 'a' and s[i-1] == 'b':
                return False
        return True