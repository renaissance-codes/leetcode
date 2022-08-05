package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/25
 */
public class S021 {
    public static void main(String[] args) {
        ListNode listNode = new ListNode(1);
        ListNode listNode1 = new ListNode(2);
        ListNode listNodea = new ListNode(1);
        ListNode listNodea1 = new ListNode(2);
        ListNode listNode2 = new ListNode(3);
        ListNode listNodea2 = new ListNode(4);
        listNode.next = listNode1;
        listNode1.next = listNode2;
        listNodea.next = listNodea1;
        listNodea1.next = listNodea2;

        S021 s021 = new S021();
        s021.mergeTwoLists(listNode,listNodea);
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode listNode = head;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                listNode.next = l1;
                l1 = l1.next;
            } else {
                listNode.next = l2;
                l2 = l2.next;
            }
            listNode = listNode.next;
        }
        listNode.next = l1 == null ? l2 : l1;
        return head.next;
    }
}
