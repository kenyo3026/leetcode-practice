class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        step, step_so_far = 0, 0
        reach_so_far = 0

        for i in range(n):

            if i > reach_so_far:
                return -1

            reach_so_far = max(reach_so_far, i + nums[i])

            if i == step_so_far:
                step += 1
                step_so_far = reach_so_far

                if reach_so_far >= n - 1:
                    return step
