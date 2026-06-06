class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = 0
        right_sum, right_delay_decline = sum(nums), 0
        diff_sums = []

        for i in range(n):
            left_sum += nums[i]
            right_sum -= right_delay_decline
            right_delay_decline = nums[i]

            diff_sums.append(abs(left_sum - right_sum))

        return diff_sums