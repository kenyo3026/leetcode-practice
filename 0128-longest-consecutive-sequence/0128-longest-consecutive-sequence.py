class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        max_seq = 0

        for num in nums:

            if num in visited:
                continue

            if not num - 1 in nums:
                seq_so_far = 1
                visited.add(num)

                while num + seq_so_far in nums:
                    seq_so_far += 1
                    visited.add(num + seq_so_far)

                max_seq = max(max_seq, seq_so_far)

        return max_seq