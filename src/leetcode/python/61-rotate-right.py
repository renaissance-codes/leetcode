"""
Author  :   https://github.com/xixici
Date    :   2019/8/19
"""


# Definition for singly-linked list.
# class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next
        k %= length
        if k == 0:
            return head
        fastCur, slowCur, pre, last = head, head, None, None
        while k > 0:
            fastCur = fastCur.next
            k -= 1
        while fastCur:
            last = fastCur
            fastCur = fastCur.next
            pre = slowCur
            slowCur = slowCur.next
        pre.next = None
        last.next = head
        return slowCur