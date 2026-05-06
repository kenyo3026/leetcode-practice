# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        for _ in range(n):
            fast = fast.next

        # if fast reaches None after n steps, the node to remove is head itself
        # e.g. [1,2,3] n=3 → return [2,3]
        # e.g. [1] n=1 → return None
        if not fast:
            return head.next

        # stop when fast reaches the last node (not None)
        # so slow stops at the node just before the target
        # e.g. [1,2,3,4,5] n=2: slow=3, fast=5 → slow.next is the target (4)
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
