class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        dsum = 0
        for i in range(n):
            for j in range(i, n+1):
                dsum += len(set(nums[i:j])) ** 2

        return dsum