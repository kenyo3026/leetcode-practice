class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        max_so_far = 1

        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i]+1)

                if dp[j] > max_so_far:
                    max_so_far = dp[j]

        return max_so_far