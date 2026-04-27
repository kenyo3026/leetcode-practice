class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_length = (m + n + 1) // 2
        left_left, left_right = 0, m

        while left_left <= left_right:
            i = (left_left + left_right) // 2
            j = left_length - i

            nums1_max_left  = nums1[i-1] if i > 0 else float('-inf')
            nums1_min_right = nums1[i]   if i < m else float('inf')
            nums2_max_left  = nums2[j-1] if j > 0 else float('-inf')
            nums2_min_right = nums2[j]   if j < n else float('inf')

            if nums1_max_left <= nums2_min_right and nums2_max_left <= nums1_min_right:
                if (m + n) % 2 == 1:
                    return float(max(nums1_max_left, nums2_max_left))
                else:
                    return (max(nums1_max_left, nums2_max_left) + min(nums1_min_right, nums2_min_right)) / 2

            elif nums1_max_left > nums2_min_right:
                left_right = i - 1
            else:
                left_left = i + 1

        return 0.0