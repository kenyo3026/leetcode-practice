class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for i in range(n):
            sum_so_far = 0

            for j in range(i, min(i+r, n)):
                sum_so_far += nums[j]

                if j - i >= l - 1 and sum_so_far > 0:
                    min_sum = min(min_sum, sum_so_far)

        return min_sum if min_sum != float('inf') else -1