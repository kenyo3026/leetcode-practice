class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        nn = n * n
        matrix = [[0] * n for _ in range(n)]
        visited = set()

        d = 0
        x, y = 0, 0
        for i in range(1, nn + 1):
            matrix[x][y] = i
            visited.add((x, y))

            nx, ny = x + dirs[d][0], y + dirs[d][1]

            if not (0 <= nx < n and 0 <= ny < n and not (nx, ny) in visited):
                d = (d + 1) % 4
                nx, ny = x + dirs[d][0], y + dirs[d][1]

            x, y = nx, ny

        return matrix
