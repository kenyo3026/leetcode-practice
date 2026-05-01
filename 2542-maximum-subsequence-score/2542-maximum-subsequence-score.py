class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        max_subseq_score = 0
        min_heap_for_nums1 = []
        sum_so_far = 0

        for n2, n1 in pairs:
            heapq.heappush(min_heap_for_nums1, n1)
            sum_so_far += n1

            if len(min_heap_for_nums1) > k:
                sum_so_far -= heapq.heappop(min_heap_for_nums1)

            if len(min_heap_for_nums1) == k:
                max_subseq_score = max(max_subseq_score, sum_so_far * n2)

        return max_subseq_score