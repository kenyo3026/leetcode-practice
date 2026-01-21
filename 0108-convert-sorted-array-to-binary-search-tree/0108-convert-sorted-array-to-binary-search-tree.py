# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def divide_and_conquer(left, right):
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            if nums[left: mid]:
                root.left = divide_and_conquer(left, mid)
            if nums[mid + 1: right]:
                root.right = divide_and_conquer(mid + 1, right)

            return root

        return divide_and_conquer(0, len(nums))