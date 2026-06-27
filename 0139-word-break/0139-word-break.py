class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [True] + [False] * n

        for j in range(1, n+1):
            for i in range(j):
                if dp[i] == True and s[i:j] in word_set:
                    dp[j] = True
                    break

        return dp[-1]