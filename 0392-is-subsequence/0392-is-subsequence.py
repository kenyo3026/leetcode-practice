class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        sl, tl = len(s), len(t)
        slow = 0

        for fast in range(tl):

            if t[fast] == s[slow]:
                slow += 1

            if slow == sl:
                return True

        return False