class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([1 for pattern in patterns if pattern in word])