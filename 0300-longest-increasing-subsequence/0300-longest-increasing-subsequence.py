class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            smallers = [dp[j] for j in range(i) if nums[j] < nums[i]]
            if smallers:
                dp[i] = max(smallers) + 1

        return max(dp)
        