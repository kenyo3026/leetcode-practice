class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_stat = Counter(tuple(row) for row in grid)

        found = 0
        for col in zip(*grid):
            found += row_stat.get(col, 0)
        return found