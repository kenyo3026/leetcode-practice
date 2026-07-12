class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        # rank = [0] * n
        degree = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            x_root, y_root = find(x), find(y)

            if x_root != y_root:
                parent[y_root] = x_root

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