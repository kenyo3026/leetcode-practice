class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m

        while left < right:
            mid = (left + right) // 2
            i, j = mid // m, mid % m

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid
            else:
                left = mid + 1

        return False