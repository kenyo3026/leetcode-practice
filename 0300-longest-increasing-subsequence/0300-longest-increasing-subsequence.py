class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            candidates = [dp[j] for j in range(i) if nums[i] > nums[j]]
            if candidates:
                dp[i] = max(candidates) + 1

        return max(dp)