class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        k_smallest = []

        heap = [(nums1[0]+nums2[j], 0, j) for j in range(n2)]
        heapq.heapify(heap)

        while heap and len(k_smallest) < k:
            _, i, j = heapq.heappop(heap)
            k_smallest.append([nums1[i], nums2[j]])

            if i + 1 < n1:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))

        return k_smallest
