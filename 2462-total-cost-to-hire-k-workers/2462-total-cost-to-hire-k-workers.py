class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs = deque(costs)
        heap_left, heap_right = [], []
        total_cost = 0

        for _ in range(min(candidates, len(costs))):
            heapq.heappush(heap_left, costs.popleft())

        for _ in range(min(candidates, len(costs))):
            heapq.heappush(heap_right, costs.pop())

        for _ in range(k):

            if heap_left and heap_right:
                if heap_left[0] <= heap_right[0]:
                    total_cost += heapq.heappop(heap_left)
                    if costs:
                        heapq.heappush(heap_left, costs.popleft())
                else:
                    total_cost += heapq.heappop(heap_right)
                    if costs:
                        heapq.heappush(heap_right, costs.pop())    

            elif heap_left:
                total_cost += heapq.heappop(heap_left)
                if costs:
                    heapq.heappush(heap_left, costs.popleft())

            elif heap_right:
                total_cost += heapq.heappop(heap_right)
                if costs:
                    heapq.heappush(heap_right, costs.pop())

        return total_cost