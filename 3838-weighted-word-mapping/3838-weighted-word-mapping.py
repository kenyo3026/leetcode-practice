class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        weighted_word = ''
        for word in words:

            wc = 0
            for char in word:
                idx = ord(char) - ord('a')
                w = weights[idx]
                wc += w
            wc %= 26
            wc = 26 - wc - 1
            weighted_word += chr(ord('a') + wc)

        return weighted_word
