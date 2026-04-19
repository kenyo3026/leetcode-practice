# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total_matches = 0

        def dfs(node, prefix_sums):
            if not node:
                return

            prefix_sums = [prefix_sum + node.val for prefix_sum in prefix_sums]
            prefix_sums.append(node.val)
            for prefix_sum in prefix_sums:
                self.total_matches += (prefix_sum == targetSum)

            dfs(node.left, prefix_sums)
            dfs(node.right, prefix_sums)

        dfs(root, [])
        return self.total_matches