class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        _min, _max = min(nums), max(nums)
        _min_idx, _max_idx = nums.index(_min), nums.index(_max)

        _left_offset = min(_min_idx, _max_idx)
        _right_offset = max(_min_idx, _max_idx)

        return min(
            _right_offset + 1,
            n - _left_offset,
            (_left_offset + 1) + (n - _right_offset)
        )