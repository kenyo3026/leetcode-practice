class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(num):
            _sum = 0
            while num:
                div, mod = num//10, num%10
                num = div
                _sum += mod

            return _sum

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        num_sorted_pos = {num: i for i, num in enumerate(sorted_nums)}

        cycles = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue

            cycles += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = num_sorted_pos[nums[j]]

        return n - cycles