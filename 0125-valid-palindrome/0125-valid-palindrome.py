class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue

            if not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True