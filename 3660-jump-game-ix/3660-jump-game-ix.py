class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        jumped = [0] * n

        prefix_max = [nums[0]] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_min = [float('inf')] * (n + 1)
        for i in range(n-1, -1, -1):
            if prefix_max[i] > suffix_min[i+1]:
                jumped[i] = jumped[i+1]
            else:
                jumped[i] = prefix_max[i]
            suffix_min[i] = min(suffix_min[i+1], nums[i])

        return jumped[:n]