class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest_consecutive = 0
        heapq.heapify(nums)

        hash = {}
        for _ in range(n):
            num = heapq.heappop(nums)

            if num in hash:
                continue

            if not num - 1 in hash:
                hash[num] = 1
            else:
                hash[num] = hash[num-1] + 1

            longest_consecutive = max(longest_consecutive, hash[num])

        return longest_consecutive
                
    