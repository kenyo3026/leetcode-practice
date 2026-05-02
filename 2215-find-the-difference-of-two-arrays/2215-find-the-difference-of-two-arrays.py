class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        n1, n2 = len(nums1), len(nums2)
        diff1, diff2 = set(), set()

        for i in range(max(n1, n2)):

            if i < n1 and not nums1[i] in nums2_set and not nums1[i] in diff1:
                diff1.add(nums1[i])

            if i < n2 and not nums2[i] in nums1_set and not nums2[i] in diff2:
                diff2.add(nums2[i])

        return [list(diff1), list(diff2)]