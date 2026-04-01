# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head.next and n == 1:
        #     return None
        prev = None
        curr = head
        # 1. Reverse list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr = prev
        rev_head = curr

        # 2. Find node to remove
        count = 1
        prev = None
        while count != n:
            count += 1
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        if curr == rev_head:
            rev_head = rev_head.next
            curr.next = None

        # 3. Re-reverse list

        prev = None
        curr = rev_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr = prev
        return curr
        
        
