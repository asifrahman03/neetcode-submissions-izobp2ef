class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        def reverseLL(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # 1️⃣ Check if k nodes exist
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # 2️⃣ Isolate the group
            group_start = prev_group.next
            next_group = kth.next
            kth.next = None

            # 3️⃣ Reverse the group
            new_head = reverseLL(group_start)

            # 4️⃣ Reconnect
            prev_group.next = new_head
            group_start.next = next_group

            # Move prev_group forward
            prev_group = group_start
