class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach_so_far = 0

        for i in range(n):

            if i > reach_so_far:
                return False

            reach_so_far = max(reach_so_far, i + nums[i])

        return True