class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)

        for letter in ransomNote:

            if not letter in magazine:
                return False

            elif magazine[letter] == 0:
                return False

            magazine[letter] -= 1

        return True