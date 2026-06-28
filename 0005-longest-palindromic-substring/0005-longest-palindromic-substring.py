class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        max_str = s[0]
        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i+1)
            max_str = max(max_str, odd, even, key=len)

        return max_str