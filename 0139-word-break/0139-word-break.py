class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [True] + [False] * (n)

        def find_segpoints(curr_point):
            return [i for i in range(curr_point) if dp[i] == True]

        for j in range(n+1):
            segpoints = find_segpoints(j)
            for i in segpoints:
                if s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]