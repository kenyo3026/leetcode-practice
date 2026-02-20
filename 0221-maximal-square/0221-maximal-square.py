class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_so_far = 0

        for i in range(n):
            matrix[i][0] = int(matrix[i][0])
            if matrix[i][0] == 1:
                max_so_far = 1

        for j in range(m):
            matrix[0][j] = int(matrix[0][j])
            if matrix[0][j] == 1:
                max_so_far = 1

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = int(matrix[i][j])

                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(
                        matrix[i-1][j-1],
                        matrix[i][j-1],
                        matrix[i-1][j],
                    )
                    max_so_far = max(max_so_far, matrix[i][j])

        return max_so_far ** 2
