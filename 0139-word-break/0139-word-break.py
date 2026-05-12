class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n

        for j in range(n+1):
            segpoints = [i for i in range(j) if dp[i]==True]
            for i in segpoints:
                if s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]