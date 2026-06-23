class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        needed = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        hash = {char:0 for char in needed}

        for char in text:
            if char in hash:
                hash[char] += 1

        max_num = float('inf')
        for char, value in hash.items():
            max_num = min(max_num, hash[char] // needed[char])

        return max_num