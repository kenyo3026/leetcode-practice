class Solution:
    MOD = 10**9 + 7

    def numOfSubarrays(self, arr: list[int]) -> int:
        odd, even = 0, 1
        odd_sum_so_far = 0
        prefix = 0

        for num in arr:
            prefix += num

            if prefix % 2:
                odd += 1
                odd_sum_so_far += even
            else:
                even += 1
                odd_sum_so_far += odd

        return odd_sum_so_far % self.MOD
        