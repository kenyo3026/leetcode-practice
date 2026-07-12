class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [0] * (n + 1)
        uv_marked = None
        uv_popped = None

        for i, (u, v) in enumerate(edges):
            if parents[v] != 0:
                uv_marked = [parents[v], v]
                uv_popped = [u, v]
                edges[i][1] = -1
            else:
                parents[v] = u

        parents = list(range(n + 1))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            parents[find(y)] = find(x)

        for u, v in edges:
            if v  == -1:
                continue
            if find(u) == find(v):
                return uv_marked if uv_marked else [u, v]
            union(u, v)

        return uv_popped