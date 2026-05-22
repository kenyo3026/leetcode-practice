class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = [char for char in s]
        goal = [char for char in goal]
        n = len(s)

        for i in range(n):
            if s[-i:] + s[:-i] == goal:
                return True
        return False