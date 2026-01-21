"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(size, row, col): 
            if size == 1:
                return Node(grid[row][col], True, None, None, None, None)
            
            half = size // 2
            topleft = build(half, row, col)
            topright = build(half, row, col+half)
            bottomleft = build(half, row+half, col)
            bottomright = build(half, row+half, col+half)
            if (
                topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and 
                topleft.val == topright.val == bottomleft.val == bottomright.val
                ):
                return Node(topleft.val, True, None, None, None, None)
            return Node(1, False, topleft, topright, bottomleft, bottomright)

        return build(len(grid), 0, 0)