class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = Counter(tuple(row) for row in grid)

        result = 0
        n = len(grid)
        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            result += row_count[column]
        
        return result