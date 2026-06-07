# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_dict = {}
        child_set = set()

        for parent, child, is_left in descriptions:

            if not parent in tree_dict:
                tree_dict[parent] = TreeNode(parent)
            if not child in tree_dict:
                tree_dict[child] = TreeNode(child)

            if is_left:
                tree_dict[parent].left = tree_dict[child]
            else:
                tree_dict[parent].right = tree_dict[child]

            child_set.add(child)

        return tree_dict[next(iter(tree_dict.keys() - child_set))]