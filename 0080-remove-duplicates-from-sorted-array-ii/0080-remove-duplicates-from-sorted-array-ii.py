class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_visited = {}
        slow = 0

        for fast in range(len(nums)):
            val = nums[fast]

            if not val in hash_visited:
                hash_visited[val] = 0
            hash_visited[val] += 1

            if val in hash_visited and hash_visited[val] <= 2:
                nums[slow] = val
                slow += 1

        return slow