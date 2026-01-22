class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        max_sum, max_sum_so_far = float('-inf'), 0
        min_sum, min_sum_so_far = float('inf'), 0

        for num in nums:
            total_sum += num

            max_sum_so_far += num
            max_sum = max(max_sum, max_sum_so_far)
            if max_sum_so_far < 0:
                max_sum_so_far = 0

            min_sum_so_far += num
            min_sum = min(min_sum, min_sum_so_far)
            if min_sum_so_far > 0:
                min_sum_so_far = 0

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)