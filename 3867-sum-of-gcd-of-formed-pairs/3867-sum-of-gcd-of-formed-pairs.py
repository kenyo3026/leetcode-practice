class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] if prefix_sum[i-1] > nums[i] else nums[i]

        # def gcd(a, b):
        #     smaller = min(a, b)
        #     for i in range(smaller, 0, -1):
        #         if a % i == 0 and b % i == 0:
        #             return i
        #     return 1

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