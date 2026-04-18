# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_val = float('inf')
        vals = []

        def in_order_dfs(node):

            if not node:
                return None

            in_order_dfs(node.left)

            if vals:
                self.min_val = min(self.min_val, abs(vals[-1] - node.val))

            vals.append(node.val)

            in_order_dfs(node.right)

        in_order_dfs(root)
        return self.min_val