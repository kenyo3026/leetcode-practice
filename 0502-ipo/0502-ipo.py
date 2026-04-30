class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_min_heap = [(cap, pro) for pro, cap in zip(profits, capital)]
        heapq.heapify(capital_min_heap)

        profit_max_heap = []

        for _ in range(k):
            while capital_min_heap and capital_min_heap[0][0] <= w:
                cap, pro = heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap, -pro)

            if not profit_max_heap:
                break

            w -= heapq.heappop(profit_max_heap)

        return w