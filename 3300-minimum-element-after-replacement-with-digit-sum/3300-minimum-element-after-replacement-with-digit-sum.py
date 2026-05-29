class Solution:
    def minElement(self, nums: List[int]) -> int:
        replaced = []
        for num in nums:
            replace = 0
            while num != 0:
                num, mod = num //10, num % 10
                replace += mod
            replaced.append(replace)

        return min(replaced)