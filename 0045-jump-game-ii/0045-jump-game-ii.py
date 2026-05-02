class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        reach_so_far = 0
        step_so_far = reach_so_far

        for i in range(n):
            reach_so_far = max(reach_so_far, i + nums[i])

            if i == step_so_far:
                step_so_far = reach_so_far
                if i != n - 1:
                    step += 1

        return step