# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res
        carry = 0
        while l1 and l2:
            curr_d = l1.val + l2.val + carry
            if curr_d < 10:
                curr.next = ListNode(curr_d)
                carry = 0
            else:
                digit = curr_d % 10
                curr.next = ListNode(digit)
                carry = 1
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_d = l1.val + carry
            if curr_d < 10:
                curr.next = ListNode(curr_d)
                carry = 0
            else:
                digit = curr_d % 10
                curr.next = ListNode(digit)
                carry = 1
            curr = curr.next
            l1 = l1.next
        
        while l2:
            curr_d = l2.val + carry
            if curr_d < 10:
                curr.next = ListNode(curr_d)
                carry = 0
            else:
                digit = curr_d % 10
                curr.next = ListNode(digit)
                carry = 1
            curr = curr.next
            l2 = l2.next
        
        if carry != 0:
            curr.next = ListNode(carry)


        return res.next