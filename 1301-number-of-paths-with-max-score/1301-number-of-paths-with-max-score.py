class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(board)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)

        for i in range(n-2, -1, -1):
            if board[i][n-1] == 'X':
                break
            dp[i][n-1] = (dp[i+1][n-1][0] + int(board[i][n-1]), dp[i+1][n-1][1])

        for j in range(n-2, -1, -1):
            if board[n-1][j] == 'X':
                break
            dp[n-1][j] = (dp[n-1][j+1][0] + int(board[n-1][j]), dp[n-1][j+1][1])

        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                if board[i][j] == 'X':
                    continue

                score, count = -1, 0
                for di, dj in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    _score, _count = dp[di][dj]
                    if _score == -1:
                        continue

                    if _score > score:
                        score, count = _score, _count
                    elif _score == score:
                        count += _count

                if score == -1:
                    continue

                dp[i][j] = (
                    score + (0 if board[i][j] == 'E' else int(board[i][j])),
                    count % MOD,
                )

        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]