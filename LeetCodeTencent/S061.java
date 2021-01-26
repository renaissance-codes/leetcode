package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/26
 */
public class S061 {
    public static void main(String[] args) {
        ListNode listNode = new ListNode(1);
        ListNode listNode1 = new ListNode(2);
        ListNode listNode2 = new ListNode(3);
        listNode.next = listNode1;
        listNode1.next = listNode2;
        S061 s061 = new S061();
        s061.rotateRight(listNode,1);
    }

    public ListNode rotateRight(ListNode head, int k) {
        int length = getLength(head);
        int real_k = length % k;
        int move = length - real_k;
        ListNode listNode = head;
        while (listNode.next != null) {
            listNode = listNode.next;
        }
        listNode.next = head;
        return head;

    }

    private int getLength(ListNode head) {
        int l = 0;
        while (head != null) {
            l += 1;
            head = head.next;
        }
        return l;
    }
}
