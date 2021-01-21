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
        ListNode cur1 = head;
        listNode = cur1;
        listNode.next = null;
        cur1 = cur1.next;
        while (head != null) {
            head.next = listNode;
            listNode = head;
            head = head.next;
        }
        return listNode.next;
    }

    public static void main(String[] args) {
        S206 s206 = new S206();
        ListNode listNode = new ListNode();
        ListNode listNode2 = new ListNode();
        ListNode listNode3 = new ListNode();
        listNode.val = 3;
        listNode2.val = 2;
        listNode3.val = 0;
        listNode.next = listNode2;
        listNode2.next = listNode3;
        ListNode listNode1 = s206.reverseList(listNode);
        System.out.println(listNode1.toString());
    }

}
