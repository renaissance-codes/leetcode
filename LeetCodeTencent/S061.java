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
        ListNode listNode3 = new ListNode(4);
        ListNode listNode4 = new ListNode(5);
        listNode.next = listNode1;
        listNode1.next = listNode2;
        listNode2.next = listNode3;
        listNode3.next = listNode4;
        S061 s061 = new S061();
        s061.rotateRight(listNode, 2);
    }

    public ListNode rotateRight(ListNode head, int k) {

        int length = getLength(head);
        if (length == 0) {
            return null;
        }
        if (length == 1 || k == 0) {
            return head;
        }
        int real_k = k % length;
        int move = length - real_k;
        ListNode listNode = head;
        while (listNode.next != null) {
            listNode = listNode.next;
        }
        listNode.next = head;
        while (move > 0) {
            head = head.next;
            move -= 1;
        }
        ListNode listNode1 = head;
        while (length > 0){
            head = head.next;
            length -= 1;
            if(length == 1){
                head.next = null;
            }
        }
        return listNode1;

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
