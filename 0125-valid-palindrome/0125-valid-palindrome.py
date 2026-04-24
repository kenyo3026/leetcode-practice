class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [token.lower() for token in s if token.isalpha() or token.isdigit()]
        return s == s[::-1]