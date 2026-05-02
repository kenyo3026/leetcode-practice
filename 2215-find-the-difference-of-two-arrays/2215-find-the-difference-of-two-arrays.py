class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, nums1_hash = len(nums1), {num:0 for num in nums1}
        n2, nums2_hash = len(nums2), {num:0 for num in nums2}

        for i in range(max(n1, n2)):

            if i < n1 and not nums1[i] in nums2_hash:
                nums1_hash[nums1[i]] += 1

            if i < n2 and not nums2[i] in nums1_hash:
                nums2_hash[nums2[i]] += 1

        return [
            [num for num, count in nums1_hash.items() if count > 0],
            [num for num, count in nums2_hash.items() if count > 0],
        ]