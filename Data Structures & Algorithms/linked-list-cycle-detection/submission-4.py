# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()

        dummy = head
        while dummy.next is not None:
            if dummy not in node_set:
                node_set.add(dummy)
            else:
                return True
            dummy = dummy.next
        return False