class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        clr_id = 0
        clrs = [0 for _ in range(n)]
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                clr_id += 1
            clrs[i] = clr_id

        print(clrs)
        return [clrs[u] == clrs[v] for u, v in queries]