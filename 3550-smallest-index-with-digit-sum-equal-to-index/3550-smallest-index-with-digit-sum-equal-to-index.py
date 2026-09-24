class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def sum_digits(num:int):
            return sum(map(int, str(num)))

        for i, num in enumerate(nums):
            if i == sum_digits(num):
                return i
        return -1
