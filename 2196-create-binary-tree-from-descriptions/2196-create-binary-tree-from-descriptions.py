# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_dict = {}

        for parent, _, _ in descriptions:

            if not parent in tree_dict:
                node = TreeNode(val=parent)
                tree_dict[parent] = node

        child_set = set()
        for parent, child, is_left in descriptions:

            child_set.add(child)

            if not child in tree_dict:
                node = TreeNode(val=child)
                tree_dict[child] = node

            if is_left:
                tree_dict[parent].left = tree_dict[child]
            else:
                tree_dict[parent].right = tree_dict[child]

        root = next(iter(tree_dict.keys() - child_set))
        return tree_dict[root]