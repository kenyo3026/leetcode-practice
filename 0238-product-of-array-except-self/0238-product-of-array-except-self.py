class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sums = [1] * n
        suffix_sums = [1] * n

        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] * nums[i-1]

        # for i in range(n-2, -1, -1):
        for i in range(1, n):
            i = n - 1 - i
            suffix_sums[i] = suffix_sums[i+1] * nums[i+1]

        producted = []
        for i in range(n):
            producted.append(prefix_sums[i] * suffix_sums[i])

        return producted