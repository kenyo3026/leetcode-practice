class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        tag_empty, tag_fresh, tag_rotten = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        visited = set()

        queue = deque([])
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == tag_fresh:
                    fresh_count += 1
                elif grid[i][j] == tag_rotten:
                    queue.append((i, j))

        if fresh_count == 0 and len(queue) == 0:
            return 0

        while queue:
            n = len(queue)

            for _ in range(n):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and \
                        not (nx, ny) in visited and grid[nx][ny] == tag_fresh:
                        grid[nx][ny] = tag_rotten
                        fresh_count -= 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))

            minutes += 1

        return minutes - 1 if fresh_count == 0 else -1
