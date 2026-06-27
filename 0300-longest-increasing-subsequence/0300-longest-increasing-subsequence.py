class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for j in range(1, n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)

        return dp[-1]
