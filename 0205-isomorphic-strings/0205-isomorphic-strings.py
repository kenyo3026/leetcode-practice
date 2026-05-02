class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}

        for x, y in zip(s, t):

            if not x in hash:

                if y in hash.values():
                    return False

                hash[x] = y
                continue

            if hash[x] != y:
                return False

        return True