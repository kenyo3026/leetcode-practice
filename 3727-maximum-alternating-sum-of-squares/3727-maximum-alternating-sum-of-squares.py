class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [num ** 2 for num in nums]
        nums.sort()

        return -sum(nums[:n//2]) + sum(nums[n//2:])