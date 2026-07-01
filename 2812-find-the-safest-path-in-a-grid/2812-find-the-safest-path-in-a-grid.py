class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            self.parents[x_parent] = y_parent
            return True
        return False


class Solution:
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        n, m = len(grid), len(grid[0])
        min_thief_dist = [[None for _ in range(m)] for _ in range(n)]
        thief_pos = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        for x, y in thief_pos:
            min_thief_dist[x][y] = 0

        queue = deque(thief_pos)
        visited = set(thief_pos)
        while queue:
            x, y = queue.popleft()

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and \
                    not (nx, ny) in visited and min_thief_dist[nx][ny] == None:
                    min_thief_dist[nx][ny] = min_thief_dist[x][y] + 1
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        cells = [(x, y) for x in range(n) for y in range(m)]
        cells.sort(key=lambda x: min_thief_dist[x[0]][x[1]], reverse=True)

        uf = UnionFind(n * m)
        unlocked = set()

        start_idx = 0
        end_idx = n * m - 1

        for x, y in cells:
            unlocked.add((x, y))
            curr_idx = x * m + y

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) in unlocked:
                    neighbor_idx = nx * m + ny
                    uf.union(curr_idx, neighbor_idx)

            if uf.find(start_idx) == uf.find(end_idx):
                return min_thief_dist[x][y]

        return 0