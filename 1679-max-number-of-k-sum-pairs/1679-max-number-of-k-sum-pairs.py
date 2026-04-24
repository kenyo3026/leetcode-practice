class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        found = 0
        left, right = 0, len(nums) - 1

        while left < right:
            _sum = nums[left] + nums[right]

            if _sum == k:
                found += 1
                left += 1
                right -= 1
            elif _sum > k:
                right -= 1
            else:
                left += 1

        return found