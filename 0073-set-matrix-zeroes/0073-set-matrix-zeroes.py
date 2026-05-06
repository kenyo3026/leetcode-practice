class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        x_is_zero = set()
        y_is_zero = set()

        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 0:
                    x_is_zero.add(x)
                    y_is_zero.add(y)

        for x in range(n):
            for y in range(m):

                if matrix[x][y] == 0:
                    continue

                if x in x_is_zero or y in y_is_zero:
                    matrix[x][y] = 0

        return matrix