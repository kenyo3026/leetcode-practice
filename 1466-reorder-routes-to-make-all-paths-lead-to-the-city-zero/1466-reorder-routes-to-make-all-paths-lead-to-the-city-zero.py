class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(u, v) for u, v in connections}
        visited = set()
        self.need_flips = 0

        graphs = {}
        for u, v in edges:
            graphs[u] = graphs.get(u, [])
            graphs[u].append(v)
            graphs[v] = graphs.get(v, [])
            graphs[v].append(u)

        def dfs(city):
            visited.add(city)

            for neighbor in graphs[city]:

                if neighbor in visited:
                    continue
 
                if not (neighbor, city) in edges:
                    self.need_flips += 1

                dfs(neighbor)

        dfs(0)
        return self.need_flips