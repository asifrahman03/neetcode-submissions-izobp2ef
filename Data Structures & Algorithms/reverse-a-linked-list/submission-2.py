# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        
        dummy = head
        pD = None

        while dummy.next is not None:
            dummy = dummy.next
            head.next = pD
            pD = head
            head = dummy

        dummy.next = pD
        return dummy

        
        

        