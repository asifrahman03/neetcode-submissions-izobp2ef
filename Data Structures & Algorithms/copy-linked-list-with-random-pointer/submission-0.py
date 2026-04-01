"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        n_map = {}
        curr = head
        while curr:
            n_map[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                n_map[curr].next = n_map[curr.next]
            if curr.random:
                n_map[curr].random = n_map[curr.random]
            curr = curr.next
        
        return n_map[head]


