class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([nums[i] * nums[i] if n % (i+1) == 0 else 0 for i in range(n)])
