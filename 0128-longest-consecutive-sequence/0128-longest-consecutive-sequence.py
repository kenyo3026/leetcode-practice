class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_seq = 0

        for num in nums:

            if not num - 1 in nums:
                seq_so_far = 1

                while num + seq_so_far in nums:
                    seq_so_far += 1

                max_seq = max(max_seq, seq_so_far)

        return max_seq