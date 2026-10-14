# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = ""
        num_2 = ""

        curr = l1
        while curr:
            num_1 = str(curr.val) + num_1
            curr = curr.next
        
        curr = l2
        while curr:
            num_2 = str(curr.val) + num_2
            curr = curr.next

        if num_1 == "": total = int(num_2)
        elif num_2 == "": total = int(num_1)
        else: total = str(int(num_1) + int(num_2))

        l3 = None
        head = l3
        tmp = head
        for char in total[::-1]:
            l3 = ListNode(int(char))
            if tmp: 
                tmp.next = l3
                tmp = tmp.next
            else: 
                tmp = l3
                head = l3

        return head


