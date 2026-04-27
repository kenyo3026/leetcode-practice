class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_visited = None
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != prev_visited:
                nums[slow] = nums[fast]
                slow += 1
                prev_visited = nums[fast]

        return slow