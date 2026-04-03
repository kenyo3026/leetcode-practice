class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len = len(word1), len(word2)
        merged = []

        i, j = 0, 0
        while (i < word1_len) and (j < word2_len):

            if i < word1_len:
                merged.append(word1[i])
                i += 1

            if j < word2_len:
                merged.append(word2[j])
                j += 1

        if i < word1_len:
            merged.append(word1[i:])
        elif j < word2_len:
            merged.append(word2[j:])

        return "".join(merged)