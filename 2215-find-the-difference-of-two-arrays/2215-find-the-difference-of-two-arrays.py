class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_hash = set(nums1)
        nums2_hash = set(nums2)

        return [
            [num for num in nums1_hash if not num in nums2_hash],
            [num for num in nums2_hash if not num in nums1_hash],
        ]