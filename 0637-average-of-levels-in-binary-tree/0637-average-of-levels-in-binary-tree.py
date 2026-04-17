# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_avgs = []

        queue = deque([root])

        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if i == 0:
                    level_avgs.append(node.val)
                else:
                    level_avgs[-1] += node.val

                if i == n - 1:
                    level_avgs[-1] /= n

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return level_avgs