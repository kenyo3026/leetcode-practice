class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        num_set = set(nums)
        if len(num_set) != n - 1:
            return False

        hash = {i:1 for i in range(1, n-1)}
        hash[n-1] = 2
        fill = n - 1

        for num in nums:
            if num in hash:
                hash[num] -= 1
                if hash[num] == 0:
                    fill -= 1

        return fill == 0