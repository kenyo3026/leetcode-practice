# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_values_of_root1 = []
        leaf_values_of_root2 = []

        def dfs(node, leaf_values):
            if not node:
                return

            if not node.left and not node.right:
                leaf_values.append(node.val)

            if node.left:
                dfs(node.left, leaf_values)
            if node.right:
                dfs(node.right, leaf_values)

        dfs(root1, leaf_values_of_root1)
        dfs(root2, leaf_values_of_root2)
        return leaf_values_of_root1 == leaf_values_of_root2