# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid_bst = True
        self.prev_node_val = float('-inf')

        def in_order_dfs(node):

            if not node:
                return

            in_order_dfs(node.left)

            if not node.val > self.prev_node_val:
                self.is_valid_bst = False
                return

            self.prev_node_val = node.val

            in_order_dfs(node.right)

        in_order_dfs(root)
        return self.is_valid_bst