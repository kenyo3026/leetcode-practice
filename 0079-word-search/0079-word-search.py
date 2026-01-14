class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols = len(board), len(board[0])
        word_len = len(word)
        visited = set()

        def backtrack(x, y, idx):

            if board[x][y] != word[idx]:
                return

            if idx == word_len - 1:
                return True

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and \
                    not (nx, ny) in visited:
                    if backtrack(nx, ny, idx+1):
                        return True

            visited.remove((x, y))

        for x in range(rows):
            for y in range(cols):
                if backtrack(x, y, 0):
                    return True

        return False