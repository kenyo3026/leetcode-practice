class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1_000_000_007
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, curr_depth):
            max_depth = curr_depth
            for child in graph[node]:
                if child == parent:
                    continue
                max_depth = max(max_depth, dfs(child, node, curr_depth+1))
            return max_depth

        k = dfs(1, 0, 0)
        return pow(2, k - 1, mod)


