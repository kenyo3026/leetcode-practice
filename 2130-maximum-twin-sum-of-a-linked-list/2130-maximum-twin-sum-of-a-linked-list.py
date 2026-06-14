# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_vals = []

        node = head
        while node:
            node_vals.append(node.val)
            node = node.next

        half = (len(node_vals) // 2) + 1
        twin_sum = float('-inf')
        for i in range(half):
            twin_sum = max(twin_sum, node_vals[i] + node_vals[-(i+1)])

        return twin_sum