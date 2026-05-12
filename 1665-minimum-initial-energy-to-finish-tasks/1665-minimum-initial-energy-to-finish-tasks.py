import heapq

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        heap = [(-(m - a), a, m) for a, m in tasks]
        heapq.heapify(heap)

        consumed = 0
        min_initial = 0

        while heap:
            _, actual, minimum = heapq.heappop(heap)
            consumed += actual
            min_initial = max(min_initial, consumed - actual + minimum)

        return min_initial