# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        a,b = list1,list2
        if list1.val > list2.val:
            b,a = list1,list2

        head = a
        while a and b:
            while a.next and a.next.val <= b.val:
                a = a.next

            if not a.next:
                a.next = b
                break

            tmp = a.next
            a.next = b
            b = tmp
            a = a.next

        
        return head