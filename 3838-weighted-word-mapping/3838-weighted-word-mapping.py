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
            wc = 26 - wc
            weighted_word += chr(ord('a') + (wc - 1))

        return weighted_word
