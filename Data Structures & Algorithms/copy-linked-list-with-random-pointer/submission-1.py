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
        if not head: return head
        copy_list = {}

        curr = head
        while curr:
            copy_list[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                copy_list[curr].next = copy_list[curr.next]
            else:
                copy_list[curr].next = None

            if curr.random:
                copy_list[curr].random = copy_list[curr.random]
            else:
                copy_list[curr].random = None
            curr = curr.next

        return copy_list[head]
