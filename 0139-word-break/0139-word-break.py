class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            for j in range(i+1):
                if dp[j] == True and s[j:i+1] in word_set:
                    dp[i+1] = True

        return dp[-1]