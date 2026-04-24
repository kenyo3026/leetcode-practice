class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums) - 1
        nums.sort()
        sums = []

        for i in range(n - 1): # == len(nums) - 2

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n

            while left < right:
                _sum = nums[i] + nums[left] + nums[right]

                if _sum == 0:
                    sums.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1

        return sums