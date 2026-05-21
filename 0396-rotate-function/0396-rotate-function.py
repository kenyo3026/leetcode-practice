class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        _sum, f_sum = 0, 0
        for i in range(n):
            _sum += nums[i]
            f_sum += i * nums[i]

        max_f_sum = f_sum
        for i in range(n-1, 0, -1):
            f_sum += _sum - nums[i] * n # = 1 + n - 1
            if f_sum > max_f_sum:
                max_f_sum = f_sum

        return max_f_sum