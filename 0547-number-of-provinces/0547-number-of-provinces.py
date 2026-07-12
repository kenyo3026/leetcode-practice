class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x != y:
                parents[y] = x

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return sum(1 for x in range(n) if find(x) == x)