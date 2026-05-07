class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        found_so_far = 0

        def bfs(x, y):
            grid[x][y] = "0"
            queue = deque([(x, y)])
            visited.add((x, y))

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and \
                        not (nx, ny) in visited and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    found_so_far += 1
                    bfs(i, j)

        return found_so_far