package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/11
 */
public class S002 {
    public static void main(String[] args) {
        S002 s002 = new S002();
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);
        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);
        ListNode listNode = s002.addTwoNumbers(l1, l2);
        while (listNode != null) {
            System.out.println(listNode.val);
            listNode = listNode.next;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 初始化结果链表
        ListNode result = new ListNode(-1);
        ListNode l3 = result;
        int flag = 0;
        //循环链表1和2
        while (l1 != null && l2 != null) {
            int a = l1.val;
            int b = l2.val;
            int c = a + b + flag;
            l3.next = new ListNode(c % 10);
            flag = c >= 10 ? 1 : 0;
            l1 = l1.next;
            l2 = l2.next;
            l3 = l3.next;
        }
        //循环链表1
        while (l1 != null) {
            int a = l1.val + flag;

            l3.next = new ListNode(a % 10);

            flag = a >= 10 ? 1 : 0;
            l1 = l1.next;
            l3 = l3.next;
        }
        //循环链表2
        while (l2 != null) {
            int b = l2.val + flag;

            l3.next = new ListNode(b % 10);
            flag = b >= 10 ? 1 : 0;
            l2 = l2.next;
            l3 = l3.next;
        }
        //最终看flag如果进位，添加链表节点
        if (flag == 1) {
            l3.next = new ListNode(flag);
        }
        return result.next;
    }
}
