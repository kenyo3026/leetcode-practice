# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 1
        node = head
        while node.next:
            n += 1
            node = node.next

        k %= n
        if k == 0:
            return head

        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        head_new = slow.next
        slow.next = None
        fast.next = head

        return head_new