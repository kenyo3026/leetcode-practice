class Solution:
    def checkValidString(self, s: str) -> bool:
        _count = 0
        for char in s:
            if char == "(" or char == "*":
                _count += 1
            else:
                _count -= 1

            if _count < 0:
                return False

        _count = 0
        for char in s[::-1]:
            if char == ")" or char == "*":
                _count += 1
            else:
                _count -= 1

            if _count < 0:
                return False

        return True
