package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/25
 */
public class S023 {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode res = new ListNode(Integer.MIN_VALUE);
        for (int i = 0; i < lists.length; i++) {
            res = mergeTwoLists(lists[i], res);
        }
        return res.next;
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
