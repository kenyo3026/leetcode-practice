class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        def is_palindromic(i, j):
            if i >= j:
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            dp[i][j] = s[i] == s[j] and is_palindromic(i+1, j-1)
            return dp[i][j]

        max_palindromic = s[0]
        for i in range(n):
            for j in range(i, n):
                if is_palindromic(i, j):
                    if j - i + 1 > len(max_palindromic):
                        max_palindromic = s[i:j+1]

        return max_palindromic



            