"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {}
        copy = Node(0)
        copy_node = copy

        head_node = head
        while head_node:
            hash[head_node] = Node(head_node.val)
            head_node = head_node.next

        head_node = head
        while head_node:
            copy_node.next = hash[head_node]
            copy_node.next.next = hash.get(head_node.next, None)
            copy_node.next.random = hash.get(head_node.random, None)
            copy_node = copy_node.next
            head_node = head_node.next

        return copy.next