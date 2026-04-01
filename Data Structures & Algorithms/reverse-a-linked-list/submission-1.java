/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prevCurr = null;
        while(curr != null){
            ListNode currNext = curr.next;
            curr.next = prevCurr;
            prevCurr = curr;
            curr = currNext;
        }
        return prevCurr;
    }
}
