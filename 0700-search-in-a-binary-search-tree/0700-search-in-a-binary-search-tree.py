# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        self.res = None

        def in_order_dfs(node):

            if not node:
                return

            if node.val == self.val:
                self.res = node
                return

            in_order_dfs(node.left)
            in_order_dfs(node.right)

        in_order_dfs(root)
        return self.res