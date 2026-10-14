# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length = length + 1
            curr = curr.next
        
        pos = length - n + 1
        print(length, pos)

        if pos == 1: return head.next
        curr = head
        pos = pos - 2
        while pos:
            curr = curr.next
            pos = pos - 1

        tmp = curr.next.next
        curr.next = tmp

        return head
    