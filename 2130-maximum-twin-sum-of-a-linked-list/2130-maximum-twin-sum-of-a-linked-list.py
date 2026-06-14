# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev_node = None

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        slow_reversed = prev_node

        max_pair_sum = float('-inf')
        while slow:
            max_pair_sum = max(max_pair_sum, slow_reversed.val + slow.val)
            slow = slow.next
            slow_reversed = slow_reversed.next

        return max_pair_sum