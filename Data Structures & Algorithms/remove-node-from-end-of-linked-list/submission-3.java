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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = 0;
        ListNode lenC = head;
        while(lenC != null){
            len++;
            lenC = lenC.next;
        }
        if(len-n == 0){
            head = head.next;
            return head;
        }
        ListNode curr = head;
        ListNode prev = null;
        ListNode end= null;
        int currV = 0;
        while(currV != len-n){
            currV++;
            ListNode nC = curr.next;
            prev = curr;
            curr = nC;
            nC = nC.next;
            end = nC;
        }
        if(prev == null){
            curr = curr.next;;
        }
        if(end == null){
            prev.next = end;
        }else{
            curr.next = null;
            prev.next = end;
        }
        return head;
    }
}
