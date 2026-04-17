# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_node_values = []

        if not root:
            return level_node_values

        queue = deque([root])
        level = 0
        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if i == 0:
                    level_node_values.append([node.val])
                else:
                    level_node_values[-1].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 != 0:
                level_node_values[-1].reverse()

            level += 1

        return level_node_values
                