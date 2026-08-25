class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        i = 1
        while True:
            if not (m := k * i) in nums:
                return m
            i += 1
