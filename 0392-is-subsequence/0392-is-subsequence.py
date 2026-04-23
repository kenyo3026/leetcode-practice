class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        ls, lt = len(s), len(t)
        slow, fast = 0, 0

        while fast < lt:

            if s[slow] == t[fast]:
                slow += 1

            if slow == ls:
                return True

            fast += 1

        return False