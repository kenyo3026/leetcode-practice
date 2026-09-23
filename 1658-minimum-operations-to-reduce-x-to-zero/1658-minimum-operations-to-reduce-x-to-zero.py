class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n
        elif target < 0:
            return -1

        left = 0
        acc_sum = 0
        min_step = -1
        for right in range(n):
            acc_sum += nums[right]

            while acc_sum > target:
                acc_sum -= nums[left]
                left += 1

            if acc_sum == target:
                min_step = max(min_step, right - left + 1)

        return -1 if min_step == -1 else n - min_step