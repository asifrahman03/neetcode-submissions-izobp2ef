# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if n == 1 and not head.next:
            return None
        curr = head
        prev = None
        while curr:
            cN = curr.next
            curr.next = prev
            prev = curr
            curr = cN
        curr_remove = prev
        curr_r_p = None
        while n-1 != 0:
            n-=1
            curr_r_p = curr_remove
            curr_remove = curr_remove.next
        if not curr_r_p:
            prev = prev.next
        else:
            curr_r_p.next = curr_remove.next
        reverse_p = None
        while prev:
            pN = prev.next
            prev.next = reverse_p
            reverse_p = prev
            prev = pN
        return reverse_p

        
        
        



        
        