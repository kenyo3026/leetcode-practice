class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i]+1)

        return max(dp)