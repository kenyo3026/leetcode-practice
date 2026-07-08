class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for u, v, dis in roads:
            graph[u] = graph.get(u, [])
            graph[u].append((v, dis))
            graph[v] = graph.get(v, [])
            graph[v].append((u, dis))

        min_score = float('inf')
        queue = deque([1])
        visited = {1}
        while queue:
            node = queue.popleft()

            for neighbor, dis in graph[node]:
                min_score = min(min_score, dis)

                if not neighbor in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return min_score