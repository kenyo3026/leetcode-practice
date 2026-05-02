class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash_for_count1 = Counter(word1)
        hash_for_count2 = Counter(word2)

        if hash_for_count1.keys() != hash_for_count2.keys():
            return False

        return Counter(hash_for_count1.values()) == Counter(hash_for_count2.values())