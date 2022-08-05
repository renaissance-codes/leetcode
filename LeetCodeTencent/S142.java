package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/25
 */
public class S142 {
    public static void main(String[] args) {

        ListNode listNode = new ListNode(1);
        ListNode listNode1 = new ListNode(2);
        ListNode listNode2 = new ListNode(3);
        listNode.next = listNode1;
        listNode1.next = listNode2;
        listNode2.next = listNode1;
        S142 s142 = new S142();
        System.out.println(s142.detectCycle(listNode));
    }

    public ListNode detectCycle(ListNode head) {
        ListNode slower = head;
        ListNode faster = head;
        boolean cycle = false;
        while (faster != null && faster.next != null) {
            slower = slower.next;
            faster = faster.next.next;
            if (slower == faster) {
                cycle = true;
                break;
            }
        }
        if (cycle) {
            ListNode cur = head;
            while (cur != faster) {
                cur = cur.next;
                faster = faster.next;
            }
            return faster;
        }
        return null;

    }
}
