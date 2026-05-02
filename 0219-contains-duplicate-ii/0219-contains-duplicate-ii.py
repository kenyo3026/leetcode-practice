class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        last_index = {}

        for i in range(n):

            if nums[i] in last_index and i - last_index[nums[i]] <= k:
                return True

            last_index[nums[i]] = i

        return False