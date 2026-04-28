class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_so_far = 0

        def bfs(i, j):
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                visited.add((x, y))

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and \
                        not (nx, ny) in visited and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_so_far += 1
                    bfs(row, col)

        return island_so_far