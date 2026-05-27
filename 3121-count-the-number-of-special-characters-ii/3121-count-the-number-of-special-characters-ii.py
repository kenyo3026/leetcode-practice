class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        stats = {}
        for char in word:
            if char.islower():
                if not char in stats:
                    stats[char] = 1
                else:
                    stats[char] += 1

        founds = 0
        for char in word:
            if char.islower():
                stats[char] -= 1
            elif char.isupper():
                char_lower = char.lower()
                if stats.get(char_lower, -1) == 0:
                    founds += 1
                    stats[char_lower] = -1
                else:
                    stats[char_lower] = -1

        return founds