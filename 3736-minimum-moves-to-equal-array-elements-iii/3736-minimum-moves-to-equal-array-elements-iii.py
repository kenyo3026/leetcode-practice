class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        min_moves = 0

        for num in nums:
            min_moves += max_val - num
        return min_moves