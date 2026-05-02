class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False

        hash = {}

        for p, word in zip(pattern, s):

            if not p in hash:

                if word in hash.values():
                    return False

                hash[p] = word
                continue

            if hash[p] != word:
                return False

        return True