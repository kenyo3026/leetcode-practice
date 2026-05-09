class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def extract_layer(l):
            top, bottom, left, right = l, m-1-l, l, n-1-l
            vector = []

            for i in range(left, right):
                vector.append(grid[top][i])

            for i in range(top, bottom):
                vector.append(grid[i][right])

            for i in range(right, left, -1):
                vector.append(grid[bottom][i])

            for i in range(bottom, top, -1):
                vector.append(grid[i][left])

            return vector

        def apply_layer(l, vector):
            top, bottom, left, right = l, m-1-l, l, n-1-l
            vector = iter(vector)

            for i in range(left, right):
                grid[top][i] = next(vector)

            for i in range(top, bottom):
                grid[i][right] = next(vector)

            for i in range(right, left, -1):
                grid[bottom][i] = next(vector)

            for i in range(bottom, top, -1):
                grid[i][left] = next(vector)

        for layer in range(min(m, n) // 2):
            vector = extract_layer(layer)
            _k = k % len(vector)
            vector[-_k:], vector[:-_k] = vector[:_k], vector[_k:]

            apply_layer(layer, vector)

        return grid