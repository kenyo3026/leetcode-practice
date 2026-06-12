class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1_000_000_007
        n = len(edges) + 1
        LOG = n.bit_length()

        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        parent_binary_lifting_map = [[-1] * LOG for i in range(n+1)]

        queue = deque([1])
        visited = {1}
        while queue:
            node = queue.popleft()

            for child in graph[node]:

                if not child in visited:
                    depth[child] = depth[node] + 1
                    parent_binary_lifting_map[child][0] = node
                    queue.append(child)
                    visited.add(child)

        for node in range(1, n+1):
            for k in range(LOG):
                if not parent_binary_lifting_map[node][k-1] == -1:
                    parent_binary_lifting_map[node][k] = parent_binary_lifting_map[parent_binary_lifting_map[node][k-1]][k-1]


        def lca(u, v):
            # make sure u is deeper
            if depth[u] < depth[v]:
                u, v = v, u

            # lift u to same depth as v
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent_binary_lifting_map[u][k]

            if u == v:
                return u

            # lift both until lca
            for k in range(LOG - 1, -1, -1):
                if parent_binary_lifting_map[u][k] != parent_binary_lifting_map[v][k]:
                    u = parent_binary_lifting_map[u][k]
                    v = parent_binary_lifting_map[v][k]

            return parent_binary_lifting_map[u][0]

        answer = []
        for u, v in queries:
            l = lca(u, v)
            path_length = depth[u] + depth[v] - 2 * depth[l]
            if path_length == 0:
                answer.append(0)
            else:
                answer.append(pow(2, path_length - 1, MOD))

        return answer
