class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        dsum = 0
        for i in range(n):
            subset = set()
            for j in range(i, n):
                subset.add(nums[j])
                dsum += len(subset) ** 2

        return dsum