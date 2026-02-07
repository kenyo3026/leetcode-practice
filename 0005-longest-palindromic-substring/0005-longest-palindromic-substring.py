class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = (length == 2) or dp[i+1][j-1]
                    if dp[i][j] and length > max_len:
                        start, max_len = i, length

        return s[start:start+max_len]



            