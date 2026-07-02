class Solution:
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        health -= grid[0][0]

        visited = set()
        queue = deque([(0, 0, health)])
        while queue:
            x, y, health_left = queue.popleft()
            if x == n - 1 and y == m - 1:
                return True

            if health == 0:
                return False

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                nxny = (nx, ny)

                if 0 <= nx < n and 0 <= ny < m and nxny not in visited:
                    if grid[nx][ny] == 0:
                        queue.appendleft((nx, ny, health_left))
                    elif grid[nx][ny] == 1 and health_left - 1 > 0:
                        queue.append((nx, ny, health_left - 1))

        return False