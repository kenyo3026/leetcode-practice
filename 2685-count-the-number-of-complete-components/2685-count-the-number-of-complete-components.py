class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        degree = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            degree[u] += 1
            degree[v] += 1

        cnt = [0] * n
        deg_sum = [0] * n
        for i in range(n):
            r = find(i)
            cnt[r] += 1
            deg_sum[r] += degree[i]

        return sum(
            cnt[r] and deg_sum[r] // 2 == cnt[r] * (cnt[r] - 1) // 2
            for r in range(n)
        )