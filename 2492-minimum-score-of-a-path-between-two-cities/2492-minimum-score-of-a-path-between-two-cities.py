class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph, graph_dis = {}, {}
        for u, v, dis in roads:
            graph[u] = graph.get(u, [])
            graph[u].append((v, dis))
            graph[v] = graph.get(v, [])
            graph[v].append((u, dis))

        min_score = float('inf')
        queue = deque([1])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)

            for neighbor, dis in graph[node]:
                min_score = min(min_score, dis)
                queue.append(neighbor)
                # visited.add(neighbor)

        return min_score