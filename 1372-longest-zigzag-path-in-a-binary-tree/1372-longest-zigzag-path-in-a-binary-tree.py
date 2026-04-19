# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.left, self.right = 0, 1
        self.max_long = 0

        def dfs(node, curr_dir, long_so_far):
            if not node:
                return

            if long_so_far > self.max_long:
                self.max_long = long_so_far

            dfs(node.left, self.left, long_so_far + 1 if curr_dir != self.left else 1)
            dfs(node.right, self.right, long_so_far + 1 if curr_dir != self.right else 1)

        dfs(root, None, 0)
        return self.max_long