# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.kth_val = None

        def in_order_dfs(node):

            if not node:
                return None

            in_order_dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.kth_val = node.val
                return

            in_order_dfs(node.right)

        in_order_dfs(root)

        return self.kth_val