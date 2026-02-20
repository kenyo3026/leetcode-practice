class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_so_far = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    matrix[i][j] = 1 + min(
                        matrix[i-1][j-1],
                        matrix[i][j-1],
                        matrix[i-1][j],
                    )
                else:
                    matrix[i][j] = 0
                    continue

                max_so_far = max(max_so_far, matrix[i][j])

        return max_so_far ** 2
