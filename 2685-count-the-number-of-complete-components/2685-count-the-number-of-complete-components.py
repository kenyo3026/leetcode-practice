class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        degree = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            # union by rank
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

        for u, v in edges:
            union(u, v)
            degree[u] += 1
            degree[v] += 1

        node_count = [0] * n
        degree_sum = [0] * n

        for i in range(n):
            root = find(i)
            node_count[root] += 1
            degree_sum[root] += degree[i]

        answer = 0
        for root in range(n):
            if node_count[root] == 0:
                continue
            cnt = node_count[root]
            edge_count = degree_sum[root] // 2
            if edge_count == cnt * (cnt - 1) // 2:
                answer += 1

        return answer