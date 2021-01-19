#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    删除链表的倒数第N个节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 定距离双指针， 40ms, 一次遍历
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        quick = head
        for i in range(n):
            quick = quick.next
        nhead = ListNode(-1)
        nhead.next = head

        last, slow = nhead, head

        while quick:
            last = slow
            slow = slow.next
            quick = quick.next

        last.next = slow.next

        return nhead.next
