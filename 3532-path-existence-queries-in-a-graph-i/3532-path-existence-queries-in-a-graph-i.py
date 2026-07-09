class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        cluster_id = 0
        cluster = [0 for i in range(n)]
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                cluster_id += 1
            cluster[i] = cluster_id

        return [(cluster[u] == cluster[v]) for u, v in queries]