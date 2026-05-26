class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash_set = set()
        special_chars = set()

        for char in word:
            if char.isupper() and char.lower() in hash_set:
                hash_set.remove(char.lower())
                special_chars.add(char.lower())
            elif char.islower() and char.upper() in hash_set:
                hash_set.remove(char.upper())
                special_chars.add(char.lower())
            else:
                hash_set.add(char)

        return len(special_chars)