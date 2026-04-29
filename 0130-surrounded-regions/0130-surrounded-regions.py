class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        visited = set()

        queue = deque([])
        for i in range(rows):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][cols-1] == 'O':
                queue.append((i, cols-1))

        for j in range(cols):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[rows-1][j] == 'O':
                queue.append((rows-1, j))

        while queue:
            x, y = queue.popleft()
            if board[x][y] != 'O':
                continue

            board[x][y] = '#'
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and \
                        (nx, ny) not in visited and board[nx][ny] == 'O':
                    queue.append((nx, ny))

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == '#':
                    board[x][y] = 'O'