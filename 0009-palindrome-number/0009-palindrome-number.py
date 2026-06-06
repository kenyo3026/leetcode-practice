class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)
        left, right = 0, -1

        while left <= len(x) // 2:
            if x[left] != x[right]:
                return False

            left += 1
            right -= 1

        return True