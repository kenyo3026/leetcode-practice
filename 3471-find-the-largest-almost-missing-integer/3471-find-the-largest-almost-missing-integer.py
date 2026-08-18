class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)

        if k == 1:
            freq = Counter(nums)
            candidates = [x for x in nums if freq[x] == 1]
            return max(candidates) if candidates else -1

        inner_set = set(nums[1:-1])
        left, right = nums[0], nums[-1]

        if left == right:
            return -1

        candidates = []
        if not left in inner_set:
            candidates.append(left)
        if not right in inner_set:
            candidates.append(right)

        return max(candidates) if candidates else -1