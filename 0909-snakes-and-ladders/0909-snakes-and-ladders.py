class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board[0])
        des = n * n

        def get_zigzag_coord(pos:int):
            row, col = (pos-1) // n, (pos-1) % n
            col = col if row % 2 == 0 else n - 1 - col
            row = n - 1 - row
            return row, col

        pos, step = 1, 1
        queue = deque([(pos, step)])
        visited = set([pos])
        while queue:
            curr_pos, step = queue.popleft()

            for i in range(1, 7):
                next_pos = curr_pos + i

                row, col = get_zigzag_coord(next_pos)

                if board[row][col] != -1:
                    next_pos = board[row][col]

                if next_pos == des:
                    return step

                if not next_pos in visited:
                    queue.append((next_pos, step+1))
                    visited.add(next_pos)

        return -1