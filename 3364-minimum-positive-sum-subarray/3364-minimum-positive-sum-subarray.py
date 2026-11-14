class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for i in range(n):
            s = 0
            for j in range(i, min(i + r, n)):
                s += nums[j]
                if j - i + 1 >= l and s > 0:
                    min_sum = min(min_sum, s)

        return min_sum if min_sum != float('inf') else -1