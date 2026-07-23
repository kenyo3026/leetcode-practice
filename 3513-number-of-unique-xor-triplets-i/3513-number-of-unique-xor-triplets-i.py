class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        ans = 0
        for i in range(n.bit_length()):
            ans += 2 ** i
        return ans + 1