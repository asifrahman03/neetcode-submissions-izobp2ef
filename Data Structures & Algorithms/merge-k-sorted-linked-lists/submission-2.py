# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge2Lists(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            
            res = ListNode(0)
            curr = res
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    curr.next = ListNode(list2.val)
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            return res.next
        
        merged = lists[0]
        for i in range(1, len(lists)):
            c_merged = merge2Lists(merged, lists[i])
            merged = c_merged
        return merged
        