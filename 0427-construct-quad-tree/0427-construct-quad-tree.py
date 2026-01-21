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
        n = len(grid)

        def divide_and_conquer(row_left, row_right, col_left, col_right):
            if row_right - row_left == 1:
                return Node(val=grid[row_left][col_left] == 1, isLeaf=True, 
                            topLeft=None, topRight=None, 
                            bottomLeft=None, bottomRight=None)

            row_mid = (row_left + row_right) // 2
            col_mid = (col_left + col_right) // 2

            topLeft = divide_and_conquer(row_left, row_mid, col_left, col_mid)
            topRight = divide_and_conquer(row_left, row_mid, col_mid, col_right)
            bottomLeft = divide_and_conquer(row_mid, row_right, col_left, col_mid)
            bottomRight = divide_and_conquer(row_mid, row_right, col_mid, col_right)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and 
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):

                return Node(val=topLeft.val, isLeaf=True, 
                            topLeft=None, topRight=None, 
                            bottomLeft=None, bottomRight=None)

            return Node(val=True, isLeaf=False, 
                        topLeft=topLeft, topRight=topRight, 
                        bottomLeft=bottomLeft, bottomRight=bottomRight)

        return divide_and_conquer(0, n, 0, n)