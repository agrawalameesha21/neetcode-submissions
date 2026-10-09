# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while slow and fast:
            if slow == None or slow.next == None or fast == None or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next
            if fast.next == None: return False

            fast = fast.next
            if slow == fast:
                return True
            
        return False

