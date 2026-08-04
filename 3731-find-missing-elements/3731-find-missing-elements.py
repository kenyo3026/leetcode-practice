class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums_set = set(nums)

        missing_nums = []
        for num in range(nums[0]+1, nums[-1]):
            if not num in nums_set:
                missing_nums.append(num)

        return missing_nums