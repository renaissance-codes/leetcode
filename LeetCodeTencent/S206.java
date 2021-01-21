package LeetCodeTencent;

import java.util.Stack;

/**
 * @author Yang Lei
 * @date 2021/1/20
 */
public class S206 {
    public ListNode reverseListByStack(ListNode head) {
        ListNode listNode = new ListNode();
        Stack<ListNode> nodeStack = new Stack<>();
        while (head != null) {
            nodeStack.push(head);
            head = head.next;
        }
        ListNode cur = listNode;
        while (!nodeStack.isEmpty()) {
            ListNode pop = nodeStack.pop();
            pop.next = null;

            cur.next = pop;
            cur = pop;
        }
        return listNode.next;
    }
    public ListNode reverseList(ListNode head) {
        ListNode listNode = new ListNode();
        ListNode cur0 = listNode;

        ListNode cur1 = head;
        while (cur1 != null) {
            cur0.next = cur1;
            cur1 = cur1.next;
        }
        return cur0.next;
    }

    public static void main(String[] args) {
        S206 s206 = new S206();
        ListNode listNode1 = new ListNode();
        ListNode listNode2 = new ListNode();
        ListNode listNode3 = new ListNode();
        ListNode listNode4 = new ListNode();
        listNode1.val = 1;
        listNode2.val = 2;
        listNode3.val = 3;
        listNode4.val = 4;
        listNode1.next = listNode2;
        listNode2.next = listNode3;
        listNode3.next = listNode4;
        ListNode listNode = s206.reverseList(listNode1);
        System.out.println(listNode.toString());
    }

}
