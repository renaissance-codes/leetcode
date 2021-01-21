package LeetCodeTencent;

import java.util.List;
import java.util.Stack;

/**
 * @author Yang Lei
 * @date 2021/1/20
 */
public class S206 {
    public ListNode reverseList(ListNode head) {
        ListNode listNode = new ListNode();
        Stack<ListNode> integers = new Stack<>();
        while (head != null){
            integers.add(head);
            integers.push(head);
            head = head.next;
        }
        if(!integers.isEmpty()){

        }

        while(!integers.isEmpty()){
            ListNode pop = integers.pop();
            ListNode listNode1 = new ListNode();
            listNode1 = pop;
            listNode1.next = null;
            listNode.next = listNode1;
            listNode = listNode1;

        }
        return listNode;
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
