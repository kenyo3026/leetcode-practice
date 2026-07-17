class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] if prefix_sum[i-1] > nums[i] else nums[i]

        prefix_gcd = []
        for i in range(n):
            prefix_gcd.append(gcd(nums[i], prefix_sum[i]))
        prefix_gcd.sort()

        half = n // 2
        left, right = 0, -1
        formed_pair_gcd = 0
        while left < half:
            formed_pair_gcd += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right += -1

        return formed_pair_gcd