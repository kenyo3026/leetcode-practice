class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if set(word1) != set(word2):
        #     return False

        hash_for_count1 = Counter(word1)
        hash_for_count2 = Counter(word2)

        if hash_for_count1.keys() != hash_for_count2.keys():
            return False

        return sorted(hash_for_count1.values()) == sorted(hash_for_count2.values())