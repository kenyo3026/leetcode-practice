class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        missing_nums = []
        cursor = 0
        i = nums[0]
        while i < nums[-1]:
            if i == nums[cursor]:
                cursor += 1
            else:
                missing_nums.append(i)
            i += 1

        return missing_nums