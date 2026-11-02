class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        middle = nums[len(nums)//2]
        return sum(abs(num - middle) for num in nums)