class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_so_far = 0
        max_sum = float('-inf')

        for num in nums:
            sum_so_far += num
            max_sum = max(max_sum, sum_so_far)

            if sum_so_far < 0:
                sum_so_far = 0

        return max_sum