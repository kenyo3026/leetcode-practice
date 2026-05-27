class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        stats = {}
        for char in word:
            if char.islower():
                if not char in stats:
                    stats[char] = 1
                else:
                    stats[char] += 1

        print(stats)
        founds = 0
        for char in word:
            if char.islower():
                stats[char] -= 1
            elif char.isupper():
                if stats.get(char.lower(), -1) == 0:
                    founds += 1
                    stats[char.lower()] = -1
                else:
                    stats[char.lower()] = -1

        return founds