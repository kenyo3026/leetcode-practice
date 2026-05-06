class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        res = []

        x, y = 0, 0
        d = 0
        while len(visited) != rows * cols:
            visited.add((x, y))
            res.append(matrix[x][y])

            nx, ny = x + dirs[d][0], y + dirs[d][1]

            if not (0 <= nx < rows and 0 <= ny < cols and not (nx, ny) in visited):
                d = (d + 1) % len(dirs)

            x, y = x + dirs[d][0], y + dirs[d][1]

        return res